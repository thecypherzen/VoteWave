#!/user/bin/python3

from models import storage
from models.users import User
from models.messages import Message

nanet = User.get("009c02c0f89e4e9e9f833d3c2e2a3d1a")

print(f"{nanet.first_name}'s Elections: ", len(nanet.elections))
print(f"{nanet.first_name}'s Polls: ", len(nanet.polls))
print(nanet.inbox.messages)
print(nanet.sent_messages)

elections = storage.all("Election")
for election in elections:
    if (sent := election.sent_messages) and len(sent):
        print(election.id)

election = storage.get("Election", "1b32f462df774fafb75cc2a81c12a5f4")

for message in election.sent_messages:
    print(message.sender is election)

