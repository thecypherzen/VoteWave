#!/usr/bin/python3

from models import storage
from models.inboxes import Inbox
from models.messages import Message

cands = storage.all("Candidate")
voters = storage.all("Voter")
# elecs = storage.all("Election")
# polls = storage.all("Poll")


for cand in cands:
    if cand.redflags:
        redflags = [flag for flag in cand.redflags if flag]
        print(f"+++[candidate {cand.id} redflags (len:{len(redflags)})]+++")
        for redflag in redflags:
            print(redflag if redflag else "")
            print()
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")



for voter in voters:
    if voter.redflags:
        redflags = [flag for flag in voter.redflags if flag]
        print(f"+++[voter {voter.id} redflags (len:{len(redflags)})]+++")
        for redflag in redflags:
            print(redflag if redflag else "")
            print()
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

