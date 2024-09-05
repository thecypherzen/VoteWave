#!/usr/bin/python3

from models import storage
from models.users import User

user1 = User(
    first_name="Ada",
    last_name="Mamis",
    password="fdcu8093x",
    security_key="eueoi8",
    email="francis.ok@gmail.com",
    dob="1987-11-12",
    prefix="Mr",
    address="Nigeria"
)

user2 = User(
    first_name="Jonah",
    dob="1990-10-23",
    password="justin",
    security_key="beat",
    email="omk@outlook.com"
)
user1_id = user1.id
user2_id = user2.id

storage.add([user1, user2])
storage.save()
storage.close()

user3 = User(
    first_name="Lekki",
    email="lekkibeats@gmail.com",
    password="ewduij",
    security_key="we9832",
    dob="1987-01-10"
)

storage.add(user3)

user4 = User(
    first_name="Timberlake",
    email="calibre@gmail.com",
    password="ewduijwe",
    security_key="we98jk32",
    dob="1987-01-12"
)

storage.add(user4)
storage.save()
res = storage.all("User")
results = list(map(lambda item: item.to_dict(), res))
for result in results:
    print(result, end='\n\n')

