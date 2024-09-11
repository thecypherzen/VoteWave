#!/usr/bin/python3

from models import storage
from models.notices import Notice
from models.metadata import Metadata

elecs = storage.all("Election")
polls = storage.all("Poll")

e1 = elecs[0]
p1 = polls[0]
notice1 = Notice(owner_id=e1.id, owner_type="election",
                 subject="Notice for Election 1",
                 body="Election date is shifted")
notice1_meta = Metadata(name="notice1_image.png",
                        location="/this/and/that",
                        owner_id=notice1.id, owner_type="notice",
                        use_as="post_img",
                        mime_type="image/png")

notice2 = Notice(owner_id=p1.id, owner_type="poll",
                 subject="Hey Poll Voters. Listen up!",
                 body="We're surprising the winner...")
notice2_meta = Metadata(name="poll_notice_img.jpg",
                        location="thia/thasd",
                        owner_id=notice2.id, owner_type="notice",
                        use_as="post_img",
                        mime_type="image/jpg")

storage.add(notice1_meta, notice2_meta)
storage.save()
storage.add(notice1, notice2)
storage.save()

print("\n\t=======ELECTION CHECKS========\n")
print("\t\t\tNOTICE\n",notice1)
print("\t\t\tNOTICE-OWNER\n",notice1.owner)
print("\t\t\tNOTICE-METADATA\n",notice1.meta_data)
print("\t\t\tNOTICE-POLL\n", notice1.poll)
print("\t\t\tNOTICE-ELECTION\n",notice1.election)

print()
print("\t\t\tMETADATA-NOTICE\n", notice1_meta.notice)
print()
print("\t\t\tELECTION-NOTICES\n", e1.notices, f"({len(e1.notices)})")

print("\n\t=======POLL CHECKS========\n")
print("\t\t\tNOTICE\n", notice2)
print("\t\t\tNOTICE-OWNER\n",notice2.owner)
print("\t\t\tNOTICE-METADATA\n",notice2.meta_data)
print("\t\t\tNOTICE-POLL\n",notice2.poll)
print("\t\t\tNOTICE-ELECTION\n", notice2.election)

print()
print("\t\t\tMETADATA-NOTICE\n", notice2_meta.notice)
print()
print("\t\t\tPOLL-NOTICES\n", p1.notices, f"({len(p1.notices)})")


print(f"destroying poll notice {notice2.id}")
print("poll.notices length before: ",len(p1.notices))
notice2.destroy()
print("poll.notices length after: ",len(p1.notices))
print("notice not in poll.notices anymore: ",
      notice2 not in p1.notices)
print("notice metadata doesn't exist anymore: ",
      storage.get("Metadata", notice2_meta.id) is None)


print(f"destroying election notice {notice1.id}")
print("election.notices length before: ",len(e1.notices))
notice1.destroy()
print("election.notices length after: ",len(e1.notices))
print("notice not in election.notices anymore: ",
      notice1 not in e1.notices)
print("notice metadata doesn't exist anymore: ",
      storage.get("Metadata", notice1_meta.id) is None)

