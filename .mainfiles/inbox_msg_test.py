#!/usr/bin/python3

from models import storage
from models.messages import Message
from models.inboxes import Inbox

elecs = storage.all("Election")
polls = storage.all("Poll")
users = storage.all("User")[:10]


for elec in elecs:
    print(f"Election {elec.id}:")
    if (ibx := elec.inbox):
        print(f"====>{elec.inbox.id}: Messages")
        if ( msgs := ibx.messages):
            print(f"=========>{msgs}")

for poll in polls:
    print(f"Poll {poll.id}:")
    if( ibx := poll.inbox):
        print(f"====>{ibx.id}: Messages")
        if (msgs := ibx.messages):
            print(f"=========>{msgs}")

for user in users:
    print(f"Users {user.id}:")
    if (ibx := user.inbox):
        print(f"====>{ibx.id}: Messages")
        if (msgs := ibx.messages):
            print(f"=========>{msgs}")


