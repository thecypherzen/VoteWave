#!/urs/bin/python3
"""defines the base activity from which polls and
    elections will inherit
"""

from sqlalchemy import Boolean, Integer, String
from sqlalchemy.ext.associationproxy import AssociationProxy, \
    association_proxy
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.base_class import Base
from models.base_activity import BaseActivity
from models.admin_polls_elections import admin_polls_elections as ape
from typing import List

class Poll(BaseActivity, Base):
    """Defines a poll class

    """
    count = 0
    __tablename__ = "polls"
    serial: Mapped[int] = \
        mapped_column(Integer, nullable=False, autoincrement=True)
    location: Mapped[str] = mapped_column(String(255), nullable=False)
    title: Mapped[str] = mapped_column(String(128), nullable=False)
    allows_anonymous: Mapped[bool] = \
        mapped_column(Boolean, nullable=False, default=True)
    allow_multi_votes: Mapped[bool] = \
        mapped_column(Boolean, nullable=False, default=True)

    # relationships
    _metadata: Mapped[List["Metadata"]] = relationship(
        back_populates="poll", overlaps="_metadata, _metadata",
        foreign_keys="Metadata.owner_id", primaryjoin="and_(Poll.id \
        == Metadata.owner_id, Metadata.owner_type == 'poll')")
    admins: Mapped[List["Admin"]] = relationship(
        secondary=ape, overlaps="admins")
    blacklist_entries: Mapped[List["Blacklist"]] = relationship(
        back_populates="poll", foreign_keys="Blacklist.poll_id",
        cascade="all, delete-orphan")
    chatroom: Mapped["Chatroom"] = relationship(
        back_populates="poll")
    inbox: Mapped["Inbox"] = relationship(
        back_populates="poll", cascade="all, delete-orphan",
        primaryjoin="and_(Inbox.owner_id == Poll.id, \
        Inbox.owner_type == 'poll')", foreign_keys="Inbox.owner_id",
        overlaps="inbox, inbox")
    invitations: Mapped[List["Invitation"]] = relationship(
        back_populates="poll", cascade="all, delete-orphan")
    owner: Mapped["User"] = relationship(back_populates="polls")
    redflags: Mapped[List["Redflag"]] = relationship(
        back_populates="poll", cascade="all, delete-orphan")
    reviews: Mapped[List["Review"]] = relationship(
        back_populates="poll", cascade="all, delete-orphan")
    sent_messages: Mapped[List["Message"]] = relationship(
        primaryjoin="and_(Message.sender_id == Poll.id, \
        Message.sender_type == 'poll')",
        overlaps="sent_messages, sent_messages",
        foreign_keys="Message.sender_id")
    voters: Mapped[List["Voter"]] = relationship(
        back_populates="poll", cascade="all, delete-orphan")

    """
    questions = relationship()
    waitlist = relatiohship()
    redflags = relationship()
    notices = relationship()
    """

    def __init__(self, *args, **kwargs):
        """Initializes a poll instance """
        if all([kwargs.get("starts_at"), kwargs.get("ends_at"),
                kwargs.get("security_key"), title := kwargs.get("title")]):
            to_delete = ["location", "title", "allows_anonymous",
                         "allows_multi_votes"]
            self.title = title
            self.location = "votewave/user_id/polls/poll_id"
            self.allows_anonymous = kwargs.get("allows_anonymous") or True
            self.allows_multi_votes = kwargs.get('allows_multi_votes') or True
            for item in to_delete:
                if kwargs.get(item):
                    del kwargs[item]
            super().__init__(*args, **kwargs)

    @property
    def questions(self):
        """A getter that returns a list of a polls questions"""
        pass

    def close(self):
        """Closes down a poll from participation
         Also closes down all children of the poll
         Return: True on success, False otherwise
        """
        self.status = "closed"
        # close chatroom
        # close waitlist

    def create_question(self, content):
        """Creates a new question for a poll from given content"""
        pass

    def get_question(self, question_id):
        """Returns a question with give question_id if in polls' questions """
        pass

    def open(self):
        """Opens up a poll for participation
         Also opens up all children of the poll
         Return: True on success, False otherwise
        """
        self.status = "open"
        # open chatroom

    def update_question(self, question, delete=False):
        """Updates a poll's list of questions based on passed in values.
        - If delete is True, the question is deleted without any check.
        - If delete is False, the question's value is replaced with the
           + new value.
        - `question` is expected to be in the format:
           + `{"id": "<question_id>", "value": "<new_value>" }`

        Returns: True on success or False on failure of any or all
        """
        pass
