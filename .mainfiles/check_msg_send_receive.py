#!/usr/bin/python3

from models import storage
from models.inboxes import Inbox
from models.messages import Message

cands = storage.all("Candidate")
voters = storage.all("Voter")
elecs = storage.all("Election")
polls = storage.all("Poll")

print(f"candidates count: {len(cands)}")
for cand in cands:
    user = storage.get("User", cand.user_id)
    if not user.inbox:
        print("\tcreating cand inbox..")
        storage.add(Inbox(owner_id=user.id, owner_type="user"))
        storage.save()
    print("\t",user.inbox)

print(f"voters count: {len(voters)}")
for voter in voters:
    user = storage.get("User", voter.user_id)
    if not user.inbox:
        print("\tcreating voter inbox..")
        storage.add(Inbox(owner_id=user.id, owner_type="user"))
        storage.save()
    print("\t",user.inbox.id)

print(f"elections count: {len(elecs)}")
for elec in elecs:
    if not elec.inbox:
        print("\tcreating election inbox..")
        storage.add(Inbox(owner_id=elec.id, owner_type="election"))
        storage.save()
    print("\t",elec.inbox.id)

print(f"polls count: {len(polls)}")
for poll in polls:
    if not poll.inbox:
        print("\tcreating election inbox..")
        storage.add(Inbox(owner_id=poll.id, owner_type="poll"))
        storage.save()
    print("\t",poll.inbox.id)

cand1 = cands[0]

print(f"elec1 inbox msgs before: {len(elecs[0].inbox.messages)}")
print(f"elec1 sent msgs before: {len(elecs[0].sent_messages)}\n")

print(f"poll1 inbox msgs before: {len(polls[0].inbox.messages)}")
print(f"poll1 sent msgs before: {len(polls[0].sent_messages)}\n")

print(f"cand1 inbox msgs before: {len(cands[0].inbox.messages)}")
print(f"cand1 sent msgs before: {len(cands[0].sent_messages)}\n")

print(f"voter1 inbox msgs before: {len(voters[0].inbox.messages)}")
print(f"voter1 sent msgs before: {len(voters[0].sent_messages)}")

mes1 = Message(body="Message from voter 1", sender_id=voters[0].id,
               sender_type="voter", receiver_id=polls[0].id,
               receiver_type="poll",
               subject=f"Poll-{polls[0].serial} Message")
mes2 = Message(body="Message from candidate 1", sender_id=cands[0].id,
               sender_type="candidate", receiver_id=elecs[0].id,
               receiver_type="election",
               subject=f"Election-{elecs[0].serial} Message")
storage.add(mes1, mes2)
storage.save()
mes1.send()
mes2.send()



print('\n\n............RESULTS..........')
print(f"elec1 inbox msgs after: {len(elecs[0].inbox.messages)}")
print(f"elec1 sent msgs after: {len(elecs[0].sent_messages)}\n")

print(f"poll1 inbox msgs after: {len(polls[0].inbox.messages)}")
print(f"poll1 sent msgs after: {len(polls[0].sent_messages)}\n")

print(f"cand1 inbox msgs after: {len(cands[0].inbox.messages)}")
print(f"cand1 sent msgs after: {len(cands[0].sent_messages)}\n")

print(f"voter1 inbox msgs after: {len(voters[0].inbox.messages)}")
print(f"voter1 sent msgs after: {len(voters[0].sent_messages)}")


print('\n\n............SEND/RECEIVE CONTENT CHECKS..........')
print(f"msg1 in poll1 inbox: ", mes1 in polls[0].inbox.messages)
print(f"msg2 in elec1 inbox: ", mes2 in elecs[0].inbox.messages)

print(f"msg1 sent by voter1: ", mes1 in voters[0].sent_messages)
print(f"msg2 sent by cand1: ", mes2 in cands[0].sent_messages)

