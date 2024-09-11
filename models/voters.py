#!/usr/bin/python3

from sqlalchemy import Boolean, ForeignKey, Integer, String
from sqlalchemy.ext.associationproxy import AssociationProxy, \
    association_proxy
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.base_class import Base, BaseClass
from typing import List


class Voter(BaseClass, Base):
    """Defines a voter class"""
    count = 0
    __tablename__ = "voters"
    serial: Mapped[str] = mapped_column(
        Integer, nullable=False, autoincrement=True)
    user_id: Mapped[str] = mapped_column(
        ForeignKey("users.id"), nullable=False)
    election_id: Mapped[str] = mapped_column(
        ForeignKey("elections.id"), nullable=True)
    poll_id: Mapped[str] = mapped_column(
        ForeignKey("polls.id"), nullable=True)
    has_voted: Mapped[bool] = mapped_column(
        Boolean, nullable=False, default=False)
    is_anonymous: Mapped[bool] = mapped_column(
        Boolean, nullable=False, default=False)

    # relationships
    election: Mapped["Election"] = relationship(back_populates="voters")
    poll: Mapped["Poll"] = relationship(back_populates="voters")
    reviews: Mapped[List["Review"]] = \
        relationship(back_populates="voter", cascade="all, delete-orphan")
    sent_messages: Mapped[List["Message"]] = relationship(
        primaryjoin="and_(Message.sender_id == Voter.id, \
        Message.sender_type == 'voter')",
        foreign_keys="Message.sender_id",
        overlaps="sent_messages, sent_messages")

    # association proxies
    redflags: AssociationProxy[List["Redflags"]] = association_proxy(
        "sent_messages", "redflag")


    def __init__(self, *args, **kwargs):
        """Initialises a voter instance """
        if kwargs and kwargs.get("user_id") and \
           any([kwargs.get("election_id"), kwargs.get("poll_id")]):
            self.user_id = kwargs.get("user_id")
            self.election_id = kwargs.get("election_id")
            self.poll_id = kwargs.get("poll_id")
            self.has_voted = False
            super().__init__()

    @property
    def inbox(self):
        """Returns the inbox associated with a voter"""
        from models import storage
        obj = storage.get("User", self.user_id)
        return obj.inbox
