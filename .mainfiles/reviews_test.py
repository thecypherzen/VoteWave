#!/usr/bin/python3

from models.polls import Poll
from models.elections import Election
from models.users import User
from models.candidates import Candidate
from models.reviews import Review
from models.voters import Voter
from models import storage


polls = storage.all(Poll)
elecs = storage.all(Election)
users = storage.all(User)
voters = storage.all(Voter)
candidates = storage.all(Candidate)

with open("reviews_res.txt", 'a') as stdout:
    print("========ELECTIONS========", file=stdout)
    for elec in elecs:
        if len(elec.reviews):
            print(f"election {elec.id}:", file=stdout)
            for rev in elec.reviews:
                print("    -> {} by {}({})".format(
                    rev.id,
                    rev.voter_id if rev.voter_id else rev.candidate_id,
                    "Voter" if rev.voter_id else "Candidate"
                ), file=stdout)
        else:
            pass
        print(file=stdout)

with open("reviews_res.txt", 'a') as stdout:
    print("\n\n========POLLS========", file=stdout)
    for  poll in polls:
        if len(poll.reviews):
            print(f"poll {poll.id}:", file=stdout)
            for rev in poll.reviews:
                print("    -> {} by {}({})".format(
                    rev.id,
                    rev.user_id if rev.user_id else \
                    rev.voter_id if rev.voter_id else "***",
                    "User" if rev.user_id else "Voter" if rev.voter_id \
                    else "***"
                ), file=stdout)
        else:
            pass
        print(file=stdout)

with open("reviews_res.txt", 'a') as stdout:
    print("\n\n========VOTERS========", file=stdout)
    for  voter in voters:
        if len(voter.reviews):
            print(f"voter {voter.id}:", file=stdout)
            for rev in voter.reviews:
                print("    -> {} by {}({})".format(
                    rev.id, rev.voter_id, "Voter"
                ), file=stdout)
        else:
            pass
        print(file=stdout)

with open("reviews_res.txt", 'a') as stdout:
    print("\n\n========CANDIDATES========", file=stdout)
    for  candi in candidates:
        if len(candi.reviews):
            print(f"candidate {candi.id}:", file=stdout)
            for rev in candi.reviews:
                print("    -> {} by {}({})".format(
                    rev.id, rev.candidate_id, "Candidate"
                ), file=stdout)
        else:
            pass
        print(file=stdout)

with open("reviews_res.txt", 'a') as stdout:
    print("\n\n========USERS========", file=stdout)
    for  user in users:
        if len(user.reviews):
            print(f"user {user.id}:", file=stdout)
            for rev in user.reviews:
                print("    -> {} by {}({})".format(
                    rev.id, rev.user_id, "User"
                ), file=stdout)
        else:
            pass
        print(file=stdout)

