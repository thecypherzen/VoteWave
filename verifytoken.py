#!/usr/bin/python3

from models import storage
from models.users import User
from models.elections import Election
from datetime import datetime, timedelta
import sys

session = storage.session()
user1 = User(
	first_name="Justine",
	last_name="Lumbenton",
	user_name="luvvyjay",
	email="luvvy.jay@holywood.com",
	password="friskie2x@",
	security_key="iTooPlay",
	dob="2001-11-13"
)
if not user1:
	print("user creation failed")
	sys.exit(1)
try:
	session.add(user1)
	session.commit()
	print("user1 id: ", user1.id, '\n')
except Exception as e:
	print(str(e))



election = Election(
	starts_at=datetime.now() + timedelta(weeks=3),
	ends_at=datetime.now() + timedelta(weeks=5),
	security_key="theTimeix38",
	user_id=user1.id, title ="Deadline Election 0x04"
)


session.add(election)
session.commit()

print("verify user password is `meandMind` :",
	user1.verify_pass_token("meandMind", password=True))
print("verify user password is `friskie2x@` :",
	user1.verify_pass_token("friskie2x@", password=True))

print("verify user security_key is `ajasko@` :",
	user1.verify_pass_token("ajasko@", password=False))
print("verify user security_key is `iTooPlay` :",
	user1.verify_pass_token("iTooPlay", password=False), '\n')

print("verify election security_key is `bambi7je` :",
	election.verify_pass_token("bambi7je", password=False))
print("verify user security_key is `theTimeix38` :",
	election.verify_pass_token("theTimeix38", password=False), '\n')
