#!/usr/bin/python3

from models.polls import Poll
from models.elections import Election
from models.users import User
from models.candidates import Candidate
from models.reviews import Review
from models.voters import Voter
from models import storage


polls = storage.all(Poll)
elecs = storage.all(Election)
users = storage.all(User)
voters = storage.all(Voter)
candidates = storage.all(Candidate)

review1 = Review(user_id=users[0].id,
                 poll_id=polls[0].id,
                 stars=3)

review2 = Review(user_id=users[1].id,
                 poll_id=polls[1].id,
                 stars=4)

review3 = Review(voter_id=voters[0].id,
                 election_id=elecs[0].id,
                 stars=2)
review3 = Review(voter_id=voters[1].id,
                 election_id=elecs[1].id,
                 stars=5)
review4 = Review(candidate_id=candidates[0].id,
                 election_id=elecs[0].id,
                 stars=4)
review5 = Review(candidate_id=candidates[0].id,
                 election_id=elecs[1].id,
                 stars=5)
review6 = Review(voter_id=voters[2].id,
                 election_id=elecs[1].id,
                 stars=5)
review7 = Review(voter_id=voters[3].id,
                 poll_id=polls[1].id,
                 stars=4)
review8 = Review(candidate_id=candidates[2].id,
                 election_id=elecs[1].id,
                 stars=3)
storage.add([review1, review2, review3, review4,
            review5, review6, review7, review8])
storage.save()
