#!/urs/bin/python3
"""defines the base activity from which polls and
    elections will inherit
"""

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.base_class import Base
from models.base_activity import BaseActivity
from models.admin_polls_elections import admin_polls_elections as ape
from typing import List


class Election(BaseActivity, Base):
    """Defines an election class

    """
    count = 0
    __tablename__ = "elections"
    serial: Mapped[int] = mapped_column(Integer, nullable=False,
                                        autoincrement=True)
    location: Mapped[str] = mapped_column(String(255), nullable=False)
    title: Mapped[str] = mapped_column(String(128), nullable=False)

    # relatinships
    admins: Mapped[List["Admin"]] = relationship(
        secondary="admin_polls_elections", overlaps="admins")
    blacklist_entries: Mapped[List["Blacklist"]] = relationship(
        back_populates="elections",
        foreign_keys="Blacklist.election_id")
    candidates: Mapped[List["Candidate"]] = relationship(
        back_populates="election", cascade="all, delete-orphan")
    chatroom: Mapped["Chatroom"] = relationship(back_populates="election")
    inbox: Mapped["Inbox"] = relationship(
        back_populates="election", cascade="all, delete-orphan",
        primaryjoin="and_(Inbox.owner_id == Election.id, \
        Inbox.owner_type == 'election')", foreign_keys="Inbox.owner_id",
        overlaps="inbox, inbox")
    invitations: Mapped[List["Invitation"]] = relationship(
        back_populates="election", cascade="all, delete-orphan")
    owner: Mapped["User"] = relationship(back_populates="elections")
    voters: Mapped[List["Voter"]] = relationship(
        back_populates="election", cascade="all, delete-orphan")
    reviews: Mapped[List["Review"]] = relationship(
        back_populates="election", cascade="all, delete-orphan")
    """
    waitlist = relatiohship()
    redflags = relationship()
    metadata = relationship()
    notices = relationship()
    """

    def __init__(self, *args, **kwargs):
        """Initializes and election instance"""
        if all([kwargs.get("starts_at"), kwargs.get("ends_at"),
                kwargs.get("security_key"), kwargs.get("user_id"),
                title := kwargs.get("title")]):
            self.title = title
            self.location = ""
            super().__init__(*args, **kwargs)

    def close(self):
        """Closes down an election from participation
         Also closes down all children of election
         Return: True on success, False otherwise
        """
        self.status = "closed"
        # close chatroom
        # close waitlist

    def create_candidate(self, info):
        """Creates a new candidate from given information
        Returns: id of creted candidate
        """
        pass

    def update_candidate(self, candidate, delete=False):
        """Updates an election candidate's information.

        If delete is True, the candidate is deleted.
         +`candidate` is expected to be a candidate's id. Else, the candidate's
         + information is updted, and `candidate` is expected in the format:
         + `{"id": "<candidate_id>", "values": {"key": "<value>"}}`

        Returns: True on success or False on failure of any or all
        """
        pass
