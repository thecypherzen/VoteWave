#!/usr/bin/python3

from models import storage
from models.messages import Message
from models.redflags import Redflag

elections = storage.all("Election")
polls = storage.all("Poll")
voters = storage.all("Voter")
cands = storage.all("Candidate")

e1 = None
e2 = None
p1 = None
p2 = None
evtr1 = None
evtr2 = None
evtr3 = None
pvtr1 = None
pvtr2 = None
pvtr3 = None
e1cand1  = None

for election in elections:
    if e1 and e2:
        break
    if not e1 and election.voters:
        e1 = election
    if not e2 and election.voters:
        e2 = election


for poll in polls:
    if p1 and  p2:
        break
    if not p1 and poll.voters:
        p1 = poll
    if not p2 and poll.voters:
        p2 = poll
for voter in voters:
    if evtr3 and pvtr3:
        break
    if not evtr3 and \
       voter not in e1.voters and \
       voter not in e2.voters:
        evtr3 = voter
    if not pvtr3 and \
       voter not in p1.voters and \
       voter not in p2.voters:
        pvtr3 = voter

evtr1 = e1.voters[0]
evtr2 = e1.voters[1]
pvtr1 = p1.voters[0]
pvtr2 = p2.voters[1]
cand1 = e1.candidates[0]
cand2 = e2.candidates[1]



rf1msg = Message(content="redflag msg 1: My votes are not showing",
                  sender_id=cand1.id, sender_type="candidate",
                  receiver_id=e1.id, receiver_type="election")

rf2msg = Message(content="redflag msg 2: My we voters cannot see voting area",
                  sender_id=evtr2.id, sender_type="voter",
                  receiver_id=e2.id, receiver_type="election")

rf3msg = Message(content="redflag msg 3: We cannot vote ooo",
                  sender_id=pvtr1.id, sender_type="voter",
                  receiver_id=p1.id, receiver_type="poll")

rf4msg = Message(content="redflag msg4: Message from non-voter",
                  sender_id=evtr3.id, sender_type="voter",
                  receiver_id=p2.id, receiver_type="poll")

print(evtr3 in e1.voters)

rf1 = Redflag(message=rf1msg)
rf2 = Redflag(message=rf2msg)
rf3 = Redflag(message=rf3msg)
rf4 = Redflag(message=rf4msg)

redflags = [rf1, rf2, rf3, rf4]
for rf in redflags:
    if not rf:
        redflags.remove(rf)

storage.add(redflags)
storage.save()

for rf in redflags:
    print(f"================ [ Redflag {rf.serial} info ] ==================")
    print(f"\tid: {rf.id}\n")
    print(f"\tmessage: {rf.message}\n")
    print(f"\telection: {rf.election}\n")
    print(f"\tpoll: {rf.poll}\n")
    print(f"\treceiver: {rf.receiver}\n")
    print(f"\tauthor: {rf.author}")
    print(f"===================================================================")

print("============TREAT TEST==========")
rf1.treat()
storage.save()
print(rf1)

