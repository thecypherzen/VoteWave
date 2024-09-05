#!/usr/bin/python3

from models import storage
from  models.blacklist import Blacklist

users = storage.all("User")[:50]
elections = storage.all("Election")
polls = storage.all("Poll")

ublist1 = Blacklist(blocked_user_id=users[19].id,
                  user_id=users[3].id,
                  reason="spam")
ublist2 = Blacklist(blocked_user_id=users[2].id,
                    user_id=users[9].id,
                    reason="bad content")
eblist1 = Blacklist(blocked_user_id=users[23].id,
                    election_id=elections[0].id,
                    reason="rigging")
eblist2 = Blacklist(blocked_user_id=users[33].id,
                    election_id=elections[0].id,
                    reason="spamming")
eblist3 = Blacklist(blocked_user_id=users[1].id,
                    election_id=elections[1].id,
                    reason="phishing")
pblist1 = Blacklist(blocked_user_id=users[38].id,
                    poll_id=polls[0].id,
                    reason="something crazy")
pblist2 = Blacklist(blocked_user_id=users[18].id,
                    poll_id=polls[0].id,
                    reason="something crazy")
pblist3 = Blacklist(blocked_user_id=users[14].id,
                    poll_id=polls[0].id,
                    reason="something crazy")
pblist4 = Blacklist(blocked_user_id=users[30].id,
                    poll_id=polls[1].id,
                    reason="something crazy")
storage.add(ublist1, ublist2, eblist1, eblist2,
            eblist3, pblist1, pblist2, pblist3, pblist4)
storage.save()
print("successfull")

