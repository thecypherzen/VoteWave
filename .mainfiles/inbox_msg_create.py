#!/usr/bin/python3

from models import storage
from models.messages import Message
from models.inboxes import Inbox

elecs = storage.all("Election")
polls = storage.all("Poll")
users = storage.all("User")[:10]

print("e 1 admins: ", elecs[0].admins)
print("e 1 candidates: ", elecs[0].candidates)
print()
print("e 1 voters: ", elecs[0].voters)
# inboxes
uib1 = Inbox(owner_id=users[0].id, owner_type="user")
uib2 = Inbox(owner_id=users[1].id, owner_type="user")
uib3 = Inbox(owner_id=users[2].id, owner_type="user")
uib4 = Inbox(owner_id=users[3].id, owner_type="user")

pib1 = Inbox(owner_id=polls[0].id, owner_type="poll")
pib2 = Inbox(owner_id=polls[1].id, owner_type="poll")

eib1 = Inbox(owner_id=elecs[0].id, owner_type="election")
eib2 = Inbox(owner_id=elecs[1].id, owner_type="election")

storage.add([uib1, uib2, uib3, uib4,
             pib1, pib2, eib1, eib2])
storage.save()
# messages
mes1 = Message(content="This is message 1", inbox_id=uib1.id)
mes2 = Message(content="This is message 2", inbox_id=uib2.id)
mes3 = Message(content="This is message 3", inbox_id=uib3.id)
mes4 = Message(content="This is message 4", inbox_id=uib1.id)
mes5 = Message(content="This is message 5", inbox_id=uib1.id)
mes6 = Message(content="This is message 6", inbox_id=uib3.id)
mes7 = Message(content="This is message 7", inbox_id=uib3.id)

mes8 = Message(content="This is message 8", inbox_id=pib1.id)
mes9 = Message(content="This is message 9", inbox_id=pib2.id)
mes10 = Message(content="This is message 10", inbox_id=eib1.id)
mes11= Message(content="This is message 11", inbox_id=eib2.id)
mes12 = Message(content="This is message 12", inbox_id=pib1.id)
mes13 = Message(content="This is message 13", inbox_id=eib1.id)
mes14 = Message(content="This is message 4", inbox_id=eib1.id)

storage.add([mes1, mes2, mes3, mes4, mes5, mes6, mes7,
             mes8, mes9, mes10, mes11, mes12, mes13, mes14])
storage.save()

