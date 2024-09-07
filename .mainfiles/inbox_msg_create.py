#!/usr/bin/python3

from models import storage
from models.messages import Message
from models.inboxes import Inbox

elecs = storage.all("Election")
elecs.sort(key=lambda obj: obj.serial)
polls = storage.all("Poll")
polls.sort(key=lambda obj: obj.serial)
users = storage.all("User")
users.sort(key=lambda obj: obj.serial)
users = users[:4]

#owners
u1 = users[0]
u2 = users[1]
u3 = users[2]
u4 = users[3]
p1 = polls[0]
p2 = polls[1]
e1 = elecs[0]
e2 = elecs[1]

# inboxes
u1ib = Inbox(owner_id=u1.id, owner_type="user")
u2ib = Inbox(owner_id=u2.id, owner_type="user")
u3ib = Inbox(owner_id=u3.id, owner_type="user")
u4ib = Inbox(owner_id=u4.id, owner_type="user")
p1ib = Inbox(owner_id=p1.id, owner_type="poll")
p2ib = Inbox(owner_id=p2.id, owner_type="poll")
e1ib = Inbox(owner_id=e1.id, owner_type="election")
e2ib = Inbox(owner_id=e2.id, owner_type="election")

storage.add([u1ib, u2ib, u3ib, u4ib, p1ib, p2ib, e1ib, e2ib])
# messages
mes1 = Message(content="This is message 1")
mes2 = Message(content="This is message 2")
mes3 = Message(content="This is message 3")
mes4 = Message(content="This is message 4")
mes5 = Message(content="This is message 5")
mes6 = Message(content="This is message 6")
mes7 = Message(content="This is message 7")

mes8 = Message(content="This is message 8")
mes9 = Message(content="This is message 9")
mes10 = Message(content="This is message 10")
mes11= Message(content="This is message 11")
mes12 = Message(content="This is message 12")
mes13 = Message(content="This is message 13")
mes14 = Message(content="This is message 4")

storage.add([mes1, mes2, mes3, mes4, mes5, mes6, mes7,
             mes8, mes9, mes10, mes11, mes12, mes13, mes14])

print("\nASSOCIATING MESSAGES TO INBOXES")
u1ib.add_message(mes1, mes4, mes7)
u2ib.add_message(mes2)
u3ib.add_message(mes3, mes4)
u4ib.add_message(mes5, mes6, mes7, mes8, mes9)
p1ib.add_message(mes10, mes11)
p2ib.add_message(mes12, mes13, mes14)
e1ib.add_message(mes6, mes8, mes12, mes13)
e2ib.add_message(mes14, mes9, mes11, mes10, mes1, mes2)

storage.save()
print("CREATING SUCCESS....")
print(f"\n===TEST USER1:{u1.id} INBOX: {u1ib.owner_id} MSGS\n")
for msg in u1ib.messages:
    print(msg)
print(f"\n===============[TESTING INBOX MESSGES MATCH]=================")
print(mes1 in u1ib.messages and mes4 in u1ib.messages
      and mes7 in u1ib.messages)
print(mes2 in u2ib.messages)
print(mes3 in u3ib.messages and mes4 in u3ib.messages)
print(mes5 in u4ib.messages and mes6 in u4ib.messages and
      mes7 in u4ib.messages and mes8 in u4ib.messages and
      mes9 in u4ib.messages)
print(mes10 in p1ib.messages and mes11 in p1ib.messages)
print(mes12 in p2ib.messages and mes13 in p2ib.messages
      and mes14 in p2ib.messages)
print(mes6 in e1ib.messages and mes8 in e1ib.messages and
      mes12 in e1ib.messages and mes13 in e1ib.messages)
print(mes14 in e2ib.messages and mes9 in e2ib.messages
      and mes11 in e2ib.messages and mes10 in e2ib.messages
      and mes1 in e2ib.messages and mes2 in e2ib.messages)

print("CHECK COMPLETE...ALL SEEMS GOOD")
