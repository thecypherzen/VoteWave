#!/usr/bin/python3

from models.users import User
from models.elections import Election
from models.candidates import Candidate
from models import storage


users = storage.all(User)
elections = storage.all(Election)

cand1 = Candidate(
    user_id=users[0].id,
    election_id=elections[0].id,
    party_name="Labour Party",
    party_initials="LP"
)

cand2 = Candidate(
    user_id=users[1].id,
    election_id=elections[0].id,
    party_name="People's Democratic Party",
    party_initials="PDP"
)

cand3 = Candidate(
    user_id=users[2].id,
    election_id=elections[1].id,
)

storage.add([cand1, cand2, cand3])
storage.save()

e1_candiates = [cand.to_dict() for  cand in elections[0].candidates]
e2_candidates = [cand.to_dict() for cand in elections[1].candidates]
print(e1_candiates)
print()
print(e2_candidates)

