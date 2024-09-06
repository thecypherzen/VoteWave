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

storage.add([election1, election2, poll1, poll2])

e1_admin1 = Admin(user_id=user1.id)
e1_admin2 = Admin(user_id=user6.id)
e2_admin1 = Admin(user_id=user2.id)
p1_admin1 = Admin( poll_id=poll1.id, user_id=user3.id )
p2_admin1 = Admin( poll_id=poll2.id, user_id=user5.id )
p2_admin2 = Admin( poll_id=poll2.id, user_id=user6.id )
p2_admin3 = Admin( poll_id=poll2.id, user_id=user4.id )

storage.add([e1_admin1, e1_admin2, e2_admin1, p1_admin1,
             p2_admin1, p2_admin2, p2_admin3])

election1.admins.extend([e1_admin1, e1_admin2])
election2.admins.extend([e2_admin1])
poll1.admins.extend([p1_admin1])
poll2.admins.extend([p2_admin1, p2_admin2, p2_admin3])

storage.save()

# querying and checking
qpoll1 = storage.get(Poll, poll1.id)
qpoll2 = storage.get(Poll, poll2.id)
qelection1 = storage.get(Election, election1.id)
qelection2 = storage.get(Election, election2.id)
qe1_admin1 = storage.get(Admin, e1_admin1.id)
qe1_admin2 = storage.get(Admin, e1_admin2.id)
qe2_admin1 = storage.get(Admin, e2_admin1.id)
qp1_admin1 = storage.get(Admin, p1_admin1.id)
qp2_admin1 = storage.get(Admin, p2_admin1.id)
qp2_admin2 = storage.get(Admin, p2_admin2.id)
qp2_admin3 = storage.get(Admin, p2_admin3.id)
print("created all..")

"""
print("poll1 id match => ", qpoll1.id == poll1.id)
print("poll2 id match => ", qpoll2.id == poll2.id)
print("election1 id match => ", qelection1.id == election1.id)
print("election2 id match => ", qelection2.id == election2.id)

e1_admins = election1.admins
e2_admins = election2.admins
p1_admins = poll1.admins
p2_admins = poll2.admins
print(e1_admins)
print("\n",e2_admins)
print("\n",p1_admins)
print("\n",p2_admins)

admins = storage.all("Admin")
for admin in admins:
    print(f"{admin.user.id}: {admin.user.first_name}")
    if (aes := admin.elections):
        for ae in aes:
            print(f"\telection:{ae.id}")
    if (aps := admin.polls):
        for ap in aps:
            print(f"\33tpoll: {ap.id}")
"""
