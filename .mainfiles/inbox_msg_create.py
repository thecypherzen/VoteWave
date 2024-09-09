#!/usr/bin/python3

from models import storage
from models.messages import Message
from models.inboxes import Inbox

polls = storage.all("Poll")[:3]
elecs = storage.all("Election")[:3]
cands = storage.all("Candidate")[:3]
admins = storage.all("Admin")
voters = storage.all("Voter")[:6]

# inboxes
print("\nCreating inboxes.....")

for poll in polls:
    if not poll.inbox:
        poll.inbox = Inbox(owner_id=poll.id, owner_type="poll")
        storage.add(poll.inbox)
        storage.save()
for elec in elecs:
    if not elec.inbox:
        elec.inbox = Inbox(owner_id=elec.id, owner_type="election")
        storage.add(elec.inbox)
        storage.save()

for cand in cands:
    user = storage.get("User", cand.user_id)
    if user and not user.inbox:
        storage.add(Inbox(owner_id=user.id, owner_type="user"))
        storage.save()

for voter in voters:
    user = storage.get("User", voter.user_id)
    if user and not user.inbox:
        storage.add(Inbox(owner_id=user.id, owner_type="user"))
        storage.save()


print("....done")

#owners
p1 = polls[0]
p2 = polls[1]
p3 = polls[2]
e1 = elecs[0]
e2 = elecs[1]
e3 = elecs[2]
c1 = cands[0]
c2 = cands[1]
c3 = cands[2]
v1 = voters[0]
v2 = voters[1]
v3 = voters[3]
v4 = voters[2]


print("\nCreating messages.....")
# messages
mes1 = Message(content="This is message 1", sender_id=e1.id,
               sender_type="election", receiver_id=v1.id,
               receiver_type="voter", admin_id=admins[0].id)
mes2 = Message(content="This is message 2", sender_id=p1.id,
               sender_type="poll", receiver_id=v2.id,
               receiver_type="voter", admin_id=admins[1].id)
mes3 = Message(content="This is message 3", sender_id=e1.id,
               sender_type="election", receiver_id=c1.id,
               receiver_type="candidate", admin_id=admins[2].id)
mes4 = Message(content="This is message 4", sender_id=e2.id,
               sender_type="election", receiver_id=c2.id,
               receiver_type="candidate", admin_id=admins[3].id)
mes5 = Message(content="This is message 5", sender_id=p1.id,
               sender_type="poll", receiver_id=v3.id,
               receiver_type="voter", admin_id=admins[4].id)
mes6 = Message(content="This is message 6", sender_id=p2.id,
               sender_type="poll", receiver_id=v2.id,
               receiver_type="voter", admin_id=admins[2].id)
mes7 = Message(content="This is message 7", sender_id=c1.id,
               sender_type="candidate", receiver_id=e1.id,
               receiver_type="election")
mes8 = Message(content="This is message 8", sender_id=c2.id,
               sender_type="candidate", receiver_id=e2.id,
               receiver_type="election")
mes9 = Message(content="This is message 9", sender_id=c3.id,
               sender_type="candidate", receiver_id=e3.id,
               receiver_type="election")
mes10 = Message(content="This is message 10", sender_id=v1.id,
                sender_type="voter", receiver_id=p1.id,
                receiver_type="poll")
mes11= Message(content="This is message 11", sender_id=v2.id,
               sender_type="voter", receiver_id=e2.id,
               receiver_type="election")
mes12 = Message(content="This is message 12", sender_id=v3.id,
                sender_type="voter", receiver_id=e1.id,
                receiver_type="election")
mes13 = Message(content="This is message 13", sender_id=v4.id,
                sender_type="voter", receiver_type="poll",
                receiver_id=p1.id)
mes14 = Message(content="This is message 4", sender_id=v3.id,
                sender_type="voter", receiver_id=p2.id,
                receiver_type="poll")

msgs = [mes1, mes2, mes3, mes4, mes5, mes6, mes7,
        mes8, mes9, mes10, mes11, mes12, mes13, mes14]
storage.add(msgs)
storage.save()
print("done....")

print("\nSending messages......")
for msg in msgs:
    res = msg.send()
    print(res)

print("done....")

print(f"\n===============[ TESTING INBOX MESSAGES ]=================")
print("msg1 in v1 inbox check: ", mes1 in v1.inbox.messages)
print("msg2 and msg6 in v2 inbox check: ",
      mes2 in v2.inbox.messages and mes6 in v2.inbox.messages)
print("msg3 in c1 inbox check: ", mes3 in c1.inbox.messages)
print("msg4 in c2 inbox check: ", mes4 in c2.inbox.messages)
print("msg5 in v3 inbox check: ", mes5 in v3.inbox.messages)
print("msg7 and msg12 in e1 inbox check: ",
      mes7 in e1.inbox.messages and mes12 in e1.inbox.messages)
print("msg8 and msg11 in e2 inbox check: ",
      mes8 in e2.inbox.messages and mes11 in e2.inbox.messages)
print("msg9 in e3 inbox check: ", mes9 in e3.inbox.messages)
print("msg10 and msg13 in p1 inbox check: ",
      mes10 in p1.inbox.messages and mes13 in p1.inbox.messages)
print("msg14 in p2 inbox check: ", mes14 in p2.inbox.messages)


print(f"\n===============[ CHECK SENT MESSAGES  ]=================")
print("msg1 sent by e1 check: ", mes1 in e1.sent_messages)
print("msg2 sent by p1 check: ", mes2 in p1.sent_messages)
print("msg3 sent by e1 check: ", mes3 in e1.sent_messages)
print("msg4 sent by e2 check: ", mes4 in e2.sent_messages)
print("msg5 sent by p1 check: ", mes5 in p1.sent_messages)
print("msg6 sent by p2 check: ", mes6 in p2.sent_messages)
print("msg7 sent by c1 check: ", mes7 in c1.sent_messages)
print("msg8 sent by c2 check: ", mes8 in c2.sent_messages)
print("msg9 sent by c3 check: ", mes9 in c3.sent_messages)
print("msg10 sent by v1 check: ", mes10 in v1.sent_messages)
print("msg11 sent by v2 check: ", mes11 in v2.sent_messages)
print("msg12 sent by v3 check: ", mes12 in v3.sent_messages)
print("msg13 sent by v4 check: ", mes13 in v4.sent_messages)
print("msg14 sent by v3 check: ", mes14 in v3.sent_messages)

print("CHECK COMPLETE...ALL SEEMS GOOD")

