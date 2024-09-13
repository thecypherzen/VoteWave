#!/usr/bin/python3

from models import storage
from models.messages import Message

messages = storage.all("Message")
print("active messages: ", len(messages))
msg1 = messages[0]
trashed = msg1.all_deleted()
print("trashed messages: ", len(trashed))

print("deleting msg: ", msg1.id)
msg1.destroy()

messages = storage.all(Message)
print("active messages: ", len(messages))
msg = messages[0]
trashed = msg.all_deleted()
print("trashed messages: ", len(trashed))
print("message {} is deleted {}".format(
    msg1.id, msg1.is_deleted))

print(f"restoring msg {msg1.id}")
msg1.restore()
print("\timessage {} is deleted {}".format(
    msg1.id, msg1.is_deleted))

