#!/usr/bin/python3

from models import storage
from models.users import User
from models.admins import Admin
from models.chatrooms import Chatroom
from models.elections import Election
from models.polls import Poll
from datetime import date, datetime, timedelta


users = storage.all(User)
user1, user2, user3, user4, user5, user6 = users[:6]


election1 = Election(
    user_id=user1.id,
    starts_at=datetime.now() + timedelta(days=4),
    ends_at=datetime.now() + timedelta(days=5),
    security_key="election1",
    title="Media department elections 2024"
)


election2 = Election(
    user_id=user2.id,
    starts_at=datetime.now() + timedelta(days=2),
    ends_at=datetime.now() + timedelta(hours=10),
    security_key="election2",
    title="CompSc Dept Election 2024"
)

poll1 = Poll(
    user_id=user3.id,
    starts_at=datetime.now() + timedelta(days=1),
    ends_at=datetime.now() + timedelta(hours=3),
    security_key="poll1",
    title="My First Poll demo"
)

poll2 = Poll(
    user_id=user5.id,
    starts_at=datetime.now() + timedelta(days=10),
    ends_at=datetime.now() + timedelta(hours=4),
    security_key="poll2",
    title="Poll Demo 2"
)


# create chatrooms
p1chat = Chatroom(poll_id=poll1.id, code=Chatroom.random_string(chars=4))
p2chat = Chatroom(poll_id=poll2.id, code=Chatroom.random_string(chars=4))
e2chat = Chatroom(election_id=election2.id, code=Chatroom.random_string(chars=4))
e1chat = Chatroom(election_id=election1.id, code=Chatroom.random_string(chars=4))

# create admins
admin1 = Admin(user_id=user1.id)
admin2 = Admin(user_id=user2.id)
admin3 = Admin(user_id=user3.id)
admin4 = Admin(user_id=user4.id)
admin5 = Admin(user_id=user5.id)

election1.admins.extend([admin1, admin2])
election2.admins.append(admin1, admin2)
poll1.admins.extend([admin1,admin2,admin3])
poll2.admins.extend([admin1, admin5, admin4])

storage.add([election1, election2, poll1, poll2])
storage.save()
storage.add([e1chat, e2chat, p1chat, p2chat])
storage.save()

print("election 1 admins:\n", election1.admins, end="\n\n")
print("election 2 admins:\n", election2.admins, end="\n\n")
print("poll1 1 admins:\n", poll1.admins, end="\n\n")
print("poll 2 aminds:\n", poll2.admins)

