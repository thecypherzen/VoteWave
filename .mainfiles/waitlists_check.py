#!/usr/bin/python3

from models import storage
from models.waitlists import Waitlist
from models.waitlists import UserWaitlist
import sys


def waitlist_user_role(user_id, waitlist_id):
    session = storage.session()
    entry = session.query(UserWaitlist).filter_by(
        user_id=user_id, waitlist_id=waitlist_id).first()
    if entry:
        return entry.join_as
    return None

polls = storage.all("Poll")
elections = storage.all("Election")
users = storage.all("User")[:5]

poll = None
election = None
for poll in polls:
    if poll.waitlist is None:
        break
for election in elections:
    if election.waitlist is None:
        break


if not poll:
    print("all polls have waitlsits. create a new one.")
    sys.exit(1)
if not election:
    print("all elections have waitlsits. create a new one.")
    sys.exit(1)


# check creation success
print("+++++++++++++[CREATING NEW WAITLISTS]+++++++++++++++")
pwait = Waitlist(owner_id=poll.id)
ewait = Waitlist(owner_id=election.id)
storage.add(pwait, ewait)
storage.save()

print("poll {} waitlist created: {}"\
      .format(poll.serial, poll.waitlist is not None))
print("\tit's the same waitlist: ", pwait is poll.waitlist)
print("election {} waitlist created: {}"\
      .format(election.serial, election.waitlist is not None))
print("\tis's the same waitlist: ", ewait is election.waitlist)

# check users on waitlist is empty
print("\npoll waitlist empty initially: {}".format(
    not len(pwait.users)))
print("election waitlist empty initially: {}".format(
    not len(ewait.users)))
if not all([not pwait.users, not ewait.users]):
    sys.exit(1)

print("\n++++++++++++[Populating poll's waitlist]+++++++++++")
for i in range(2) :
    user = users[i]
    b_len = len(user.waitlists)
    in_b4 = pwait in user.waitlists
    print(f"adding user {user.serial} to poll {poll.serial}")
    try:
        join_as = "voter" if i % 2 else "admin"
        ret = pwait.add_user(user,  join_as)
        res = ret[f"{user.serial}"]
        if not res["success"]:
            print("adding user to waitlist failed. See error below.")
            print(res["error"])
            sys.exit(1)
        print("\tverify user in waitlist: ",
              user in poll.waitlist.users)
        print(f"\tuser {user.serial } added as {join_as}: ",
              waitlist_user_role(user.id, pwait.id) == join_as)
    except Exception as e:
        print(f"\tfailed to add user {user.serial}")
    a_len = len(user.waitlists)
    in_af = pwait in user.waitlists
    print("\n\tchecking user's end...")
    print("\tuser {} waitlist len before {} <=> after {}".\
          format(user.serial, b_len, a_len))
    print("\twaitlist {} in user's waitlists before {} <=> after: {}"\
          .format(pwait.serial, in_b4, in_af))

print(f"\twaitlist length after: {len(pwait.users)}\n")

print("\n+++++++++++++[Populating election's waitlist]++++++++++++")
for i in range(2, 5):
    user = users[i]
    b_len = len(user.waitlists)
    in_b4 = ewait in user.waitlists
    print(f"adding user {user.serial} to election {election.serial}")
    try:
        join_as = "voter" if i == 2 else "admin" if i == 3 \
            else "candidate"
        ret = ewait.add_user(user,  join_as)
        res = ret[f"{user.serial}"]
        if not res["success"]:
            print("adding user to waitlist failed. See error below.")
            print(res["error"])
            sys.exit(1)
        print("\tverify user in waitlist: ",
              user in election.waitlist.users)
        print(f"\tuser {user.serial } added as {join_as}: ",
              waitlist_user_role(user.id, ewait.id) == join_as)
    except Exception as e:
        print(f"\tfailed to add user {user.serial}")
        print(e)
    a_len = len(user.waitlists)
    in_af = ewait in user.waitlists
    print("\n\tchecking user's end...")
    print("\tuser {} waitlist len before {} <=> after {}".\
          format(user.serial, b_len, a_len))
    print("\twaitlist {} in user's waitlists: {}".format(
        ewait.serial, ewait in user.waitlists))
    print("\twaitlist {} in user's waitlists before {} <=> after: {}"\
          .format(ewait.serial, in_b4, in_af))
print(f"\twaitlist length after: {len(ewait.users)}\n")


print("\n+++++++++++++[Check Activity Types]++++++++++++")
print("\twaitlist {} belongs to an election: {}".format(
    ewait.id, ewait.activity.type == "election"))
print("\twaitlist {} belongs to a poll: {}".format(
    pwait.id, pwait.activity.type == "poll"))

print("\n+++++++++++++[Checking Delete]++++++++++++")
waitlists = storage.all("Waitlist")
for waitlist in waitlists:
    if len(waitlist.users):
        user = waitlist.users[0]
        break
if not waitlist or not user:
    print("no user found on any waitlists or no waitlist at all.")
    sys.exit(1)

print("\tremoving user {} from waitlist {}...".format(
    user.serial, waitlist.serial))
ll_b4 = len(waitlist.users)
ret = waitlist.remove_user(user)
res = ret[f"{user.serial}"]
if not res["success"]:
    print("An error occured while remove user.")
    print(res["error"])
    sys.exit(1)
ll_af = len(waitlist.users)
print("\tuser {} removed successfully: {}".format(
    user.serial, ll_b4 == (ll_af + 1)))


