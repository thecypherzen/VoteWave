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
    """Defines a user class

    """
    count = 0
    __tablename__ = "elections"
    serial: Mapped[int] = mapped_column(Integer, nullable=False,
                                        autoincrement=True)
    location: Mapped[str] = mapped_column(String(255), nullable=False)
    title: Mapped[str] = mapped_column(String(128), nullable=False)
    owner: Mapped["User"] = \
        relationship(back_populates="elections")
    chatroom: Mapped["Chatroom"] = relationship(back_populates="election")
    admins: Mapped[List["Admin"]] = \
        relationship(secondary="admin_polls_elections",
                     overlap="admins")
    """
    admins = relationship()
    candidates = relationship()
    voters = relationship()
    reviews = relationship()
    waitlist = relatiohship()
    redflags = relationship()
    metadata = relationship()
    notices = relationship()
    inbox = relationship()
    """

    def __init__(self, *args, **kwargs):
        """Initializes and election instance"""
        if all([kwargs.get("starts_at"), kwargs.get("ends_at"),
                kwargs.get("security_key"), kwargs.get("user_id"),
                title := kwargs.get("title")]):
            self.title = title
            self.location = ""
            super().__init__(*args, **kwargs)

    @property
    def candidates(self):
        """A getter that returns an election's candidates """
        pass

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
