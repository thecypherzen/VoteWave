#!/usr/bin/python3
from models import storage
user = storage.all("User")[0]
inbox = storage.get("Inbox", "0ef876891501426bb921003a1c199a30")
md = storage.all("Metadata")[0]
msg = storage.all("Message")[0]


print(inbox.messages)
inbox.add_message(msg)
print([msg.to_dict() for msg in inbox.messages])
print(inbox.messages)
print("---------------------------++++---------------------------")

storage.reload()

user = storage.all("User")[0]
inbox = storage.get("Inbox", "0ef876891501426bb921003a1c199a30")
md = storage.all("Metadata")[0]
msg = storage.all("Message")[0]


print(inbox.messages)
print(f"msg {msg.id}.metadata")
msg.add_metadata(md)
print([data.to_dict() for data in msg.mdata])
storage.save()

