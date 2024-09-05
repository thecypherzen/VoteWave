#!/usr/bin/python3

from models import storage
from  models.blacklist import Blacklist
import json

users = storage.all("User")[:50]
elections = storage.all("Election")
polls = storage.all("Poll")
b_entries = storage.all("Blacklist")
u_entries = [entry for entry in b_entries if entry.user]
p_entries = [entry for entry in b_entries if entry.poll]
e_entries = [entry for entry in b_entries if entry.election]



print(f"====================[blacklist users]({len(u_entries)})===================")
for user in users:
    res = {}
    if (blacklist := user.blacklist):
        for usr in blacklist:
            i = 0
            for u_entry in u_entries:
                i += 1
                if u_entry.blocked_user_id == usr.id:
                    res[f"{i}"] = {"blocked": usr.id,
                                   "by_user": u_entry.user_id}
    if res:
        print(json.dumps(res, indent=2) + "\n")
print()


print(f"====================[blacklist polls]({len(p_entries)})===================")
for poll in polls:
    res = {}
    if (blacklist := poll.blacklist):
        for usr in blacklist:
            i = 0
            for p_entry in p_entries:
                i += 1
                if p_entry.blocked_user_id == usr.id:
                    res[f"{i}"] = {"blocked": str(usr.id),
                                   "by_poll": p_entry.poll_id}
    if res:
        print(json.dumps(res, indent=2) + "\n")
print()

print(f"====================[blacklist elections]({len(e_entries)})===================")
for election in elections:
    res = {}
    if (blacklist := election.blacklist):
        for usr in blacklist:
            i = 0
            for e_entry in e_entries:
                i += 1
                if e_entry.blocked_user_id == usr.id:
                    res[f"{i}"] = {"blocked": str(usr.id),
                                   "by_election": e_entry.election_id}
    if res:
        print(json.dumps(res, indent=2) + "\n")
print()
