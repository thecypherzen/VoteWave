#!/usr/bin/python3

from models import storage
from models.metadata import Metadata
from models.messages import MessageMetadata


user1, user2, user3 = storage.all("User")[:3]
el1, el2  = storage.all("Election")[:2]
poll1, poll2 = storage.all("Poll")[:2]
cand1, cand2, cand3 = storage.all("Candidate")[:3]
msg1, msg2, msg3, msg4, msg5 = storage.all("Message")[:5]


md1 = Metadata(name="creators.pdf", use_as="shared_content",
               mime_type="text/pdf", owner_type="poll",
               location="/path/to/poll/meta", owner_id=poll1.id)
md2= Metadata(name="alpha.html", use_as="reports",
              mime_type="text/htm.", owner_type='poll',
              location="/path/to/results", owner_id=poll1.id)
md3 = Metadata(name="myfile.txt", use_as="shared_content",
               mime_type="text/rtf", location="/path/to/meta/data",
               owner_id=user1.id, owner_type="user")
md4 = Metadata(name="mypix.png", use_as="avatar",
               mime_type="image/jpg", owner_id=user1.id,
               location="/vw/users/id/metadata/id", owner_type="user")
md5 = Metadata(name="party_logo.jpeg", use_as="avatar",
               mime_type="image/x-png", owner_id=el1.id,
               location="/vw/users/id/elecs/id/meta/id",
               owner_type="election")
md6 = Metadata(name="bgkg.png", use_as="cover_image",
               mime_type="mybg.jpeg", owner_id=el2.id,
               location="/vw/users/id/elecs/id/meta/id",
               owner_type="election")
md7 = Metadata(name="bgkg.png", use_as="cover_image",
               mime_type="mybg.jpeg", owner_type="candidate",
               location="/vw/users/id/elecs/id/meta/id",
               owner_id=cand1.id)

print("adding metadata to storage")
storage.add(md1, md2, md3, md4, md5, md6, md7)
storage.save()

print("METADATA ITEMS CREATED SUCCESSFULLY...\n")

msg1.add_metadata(md1, md7)
msg2.add_metadata(md5)
msg3.add_metadata(md4, md2, md3)
msg4.add_metadata(md6)

print("ADDED MESSAGE-METADATA ASSOC SUCCESSFULLY...\n")
print(msg1._metadata)
