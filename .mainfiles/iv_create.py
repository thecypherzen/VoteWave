#!/usr/bin/python3

from models import storage
from models.invitations import Invitation
from datetime import datetime, timedelta

elecs = storage.all("Election")
polls = storage.all("Poll")
users = storage.all("User")

iv1 = Invitation(
    user_from=users[0].id,
    user_to=users[10].id,
    link=f"vw.com/e/{elecs[0].id}/join?from={users[0].id}&to={users[10].id}",
    expires=elecs[0].ends_at,
    status=elecs[0].status,
    election_id=elecs[0].id
)
iv2 = Invitation(
    user_from=users[2].id,
    user_to=users[23].id,
    link=f"vw.com/e/{elecs[0].id}/join?from={users[2].id}&to={users[23].id}",
    expires=elecs[0].ends_at,
    status=elecs[0].status,
    election_id=elecs[0].id
)

iv3 = Invitation(
    user_from=users[4].id,
    user_to=users[44].id,
    link=f"vw.com/e/{elecs[0].id}/join?from={users[4].id}&to={users[44].id}",
    expires=elecs[0].ends_at,
    status=elecs[0].status,
    election_id=elecs[0].id
)

iv4 = Invitation(
    user_from=users[68].id,
    user_to=users[945].id,
    link=f"vw.com/e/{elecs[1].id}/join?from={users[68].id}&to={users[945].id}",
    expires=elecs[1].ends_at,
    status=elecs[1].status,
    election_id=elecs[1].id
)

iv5 = Invitation(
    user_from=users[599].id,
    user_to=users[5].id,
    link=f"vw.com/e/{elecs[1].id}/join?from={users[599].id}&to={users[5].id}",
    expires=elecs[1].ends_at,
    status=elecs[1].status,
    election_id=elecs[1].id
)

iv6 = Invitation(
    user_from=users[87].id,
    user_to=users[2].id,
    link=f"vw.com/p/{polls[0].id}/join?from={users[87].id}&to={users[2].id}",
    expires=polls[0].ends_at,
    status=polls[0].status,
    poll_id=polls[0].id
)

iv7 = Invitation(
    user_from=users[39].id,
    user_to=users[0].id,
    link=f"vw.com/p/{polls[1].id}/join?from={users[39].id}&to={users[0].id}",
    expires=polls[1].ends_at,
    status=polls[1].status,
    poll_id=polls[1].id
)

iv8 = Invitation(
    user_from=users[187].id,
    user_to=users[361].id,
    link=f"vw.com/p/{polls[1].id}/join?from={users[187].id}&to={users[361].id}",
    expires=polls[1].ends_at,
    status=polls[1].status,
    poll_id=polls[1].id
)

iv9 = Invitation(
    user_from=users[71].id,
    user_to=users[23].id,
    link=f"vw.com/p/{polls[1].id}/join?from={users[71].id}&to={users[23].id}",
    expires=polls[1].ends_at,
    status=polls[1].status,
    poll_id=polls[1].id
)

iv10 = Invitation(
    user_from=users[82].id,
    user_to=users[623].id,
    link=f"vw.com/p/{polls[1].id}/join?from={users[82].id}&to={users[623].id}",
    expires=polls[1].ends_at,
    status=polls[1].status,
    poll_id=polls[1].id
)

storage.add([iv1, iv2, iv3, iv4, iv5, iv6, iv7, iv8, iv9, iv10])
storage.save()
