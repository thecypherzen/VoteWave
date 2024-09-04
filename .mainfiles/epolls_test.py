#!/usr/bin/python3

from models import storage
from models.users import User
from models.admins import Admin
from models.chatrooms import Chatroom
from models.elections import Election
from models.polls import Poll
from datetime import date, datetime, timedelta


admins = storage.all(Admin)
print("total admins: ", len(admins))
elections = storage.all(Election)
for election in elections:
    print(election.admins)
polls = storage.all(Poll)








