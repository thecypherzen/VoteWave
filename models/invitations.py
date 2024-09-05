#!/usr/bin/python3
"""defines the user class"""


from sqlalchemy import DateTime, ForeignKey, Integer,\
    String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.base_class import Base, BaseClass
from datetime import datetime, timedelta


class Invitation(BaseClass, Base):
    count = 0

    """Defines an invitation class"""
    __tablename__ = "invitations"
    serial: Mapped[int] = mapped_column(Integer, nullable=False,
                                        autoincrement=True)
    user_from: Mapped[str] = \
        mapped_column(ForeignKey("users.id"), nullable=False)
    user_to: Mapped[str] = mapped_column(ForeignKey("users.id"), nullable=False)
    poll_id: Mapped[str] = mapped_column(ForeignKey("polls.id"), nullable=True)
    election_id: Mapped[str] = \
        mapped_column(ForeignKey("elections.id"), nullable=True)
    link: Mapped[str] = mapped_column(String(255), nullable=False)
    expires: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    # relationships
    poll: Mapped["Poll"] = relationship(back_populates="invitations")
    election: Mapped["Election"] = relationship(back_populates="invitations")
    sender: Mapped["User"] = \
        relationship(foreign_keys=[user_from], back_populates="ivs_sent")
    receiver: Mapped["User"] = \
        relationship(foreign_keys=[user_to], back_populates="ivs_received")

    __table_args__ = (UniqueConstraint("user_to", "user_from"),)

    def __init__(self, *args, **kwargs):
        """Initializes an invitation instance"""
        if kwargs and all([user_from := kwargs.get('user_from'),
                           user_to := kwargs.get("user_to"),
                           link := kwargs.get("link"),
                           any([p_id := kwargs.get("poll_id"),
                                e_id := kwargs.get("election_id")])]):
            to_delete = ["user_to", "user_from", "link", "poll_id",
                         "election_id", "expires"]
            self.user_from = user_from
            self.user_to = user_to
            self.link = link
            self.poll_id = p_id
            self.election_id = e_id
            self.expires = kwargs.get("expires") or \
                datetime.now() + timedelta(hours=1)
            for item in to_delete:
                if kwargs.get(item):
                    del kwargs[item]
            super().__init__(*args, **kwargs)

    def expired(self, inv):
        """checks if an invitation is expired or not"""
        from models import storage
        iv = storage.get("Invitation", inv.id)
        return True if datetime.now() >= iv.expires else False
