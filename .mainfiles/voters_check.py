#!/usr/bin/python3

from models.elections import Election
from models.polls import Poll
from models.users import User
from models.voters import Voter
from models import storage


elections = storage.all(Election)
users = storage.all(User)[:10]
polls = storage.all(Poll)

voters = storage.all(Voter)

with open("res.txt", "a") as stdout:
    for elec in elections:
        print(f"....election[{elec.id}]....", file=stdout)
        for e in elec.voters:
            print("  voter -> ", e.id, file=stdout)
            print("............................................", file=stdout)


with open("res.txt", "a") as stdout:
    for pol in polls:
        print(f"....poll[{pol.id}]....", file=stdout)
        for e in pol.voters:
            print("  voter -> ", pol.id, file=stdout)
            print("............................................", file=stdout)

with open("res.txt", "a") as stdout:
    for voter in voters:
        print(f"voter {voter.id} => poll: " + \
              f"[{voter.poll.id if voter.poll else None }]", file=stdout)
        print(f"voter {voter.id} => elec: " + \
              f"[{voter.election.id if voter.election else None }]", file=stdout)
