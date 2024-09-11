#!/usr/bin/python3

from models.elections import Election
from models.polls import Poll
from models.users import User
from models.voters import Voter
from models import storage


elections = storage.all(Election)
users = storage.all(User)[:10]
polls = storage.all(Poll)

e1voter1 = Voter(user_id=users[0].id, election_id=elections[0].id)
e1voter2 = Voter(user_id=users[1].id, election_id=elections[0].id)
e1voter3 = Voter(user_id=users[2].id, election_id=elections[0].id)
e1voter4 = Voter(user_id=users[3].id, election_id=elections[0].id)

e2voter1 = Voter(user_id=users[4].id, election_id=elections[1].id)
e2voter2 = Voter(user_id=users[5].id, election_id=elections[1].id)
e2voter3 = Voter(user_id=users[6].id, election_id=elections[1].id)
e2voter4 = Voter(user_id=users[7].id, election_id=elections[1].id)

p1voter1 = Voter(user_id=users[8].id, poll_id=polls[0].id)
p1voter2 = Voter(user_id=users[9].id, poll_id=polls[0].id)
p1voter3 = Voter(user_id=users[0].id, poll_id=polls[0].id)

p2voter1 = Voter(user_id=users[0].id, poll_id=polls[1].id)
p2voter2 = Voter(user_id=users[4].id, poll_id=polls[1].id)
p2voter3 = Voter(user_id=users[3].id, poll_id=polls[1].id)
p2voter4 = Voter(user_id=users[9].id, poll_id=polls[1].id)
p2voter5 = Voter(user_id=users[7].id, poll_id=polls[1].id)


storage.add([e1voter1, e1voter2, e1voter3, e1voter4,
             e2voter1, e2voter2, e2voter3, e2voter4,
             p1voter1, p1voter2, p1voter3,
             p2voter1, p2voter2, p2voter3, p2voter4, p2voter5])
storage.save()

'''
e1_voters = [e1voter1, e1voter2, e1voter3, e1voter4]
e2_voters = [e2voter1, e2voter2, e2voter3, e2voter4]
p1_voters = [p1voter1, p1voter2, p1voter3]
p2_voters = [p2voter1, p2voter2, p2voter3, p2voter4, p2voter5]
'''

voters = storage.all(Voter)

print(".....election1 voters.....")
for voter in voters:
    print("voter: ", voter.id)
    if voter.election:
        print("\tin election -> ", voter.election.id)
    else:
        print("\tin poll -> ", voter.poll.id)
    print("............................................")


