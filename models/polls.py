#!/urs/bin/python3
"""defines the base activity from which polls and
    elections will inherit
"""

from sqlalchemy import Boolean, Integer, String
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
    owner: Mapped["User"] = \
        relationship(back_populates="polls")
    chatroom: Mapped["Chatroom"] = relationship(back_populates="poll")
    admins: Mapped[List["Admin"]] = \
        relationship(secondary=ape, overlaps="admins")
    voters: Mapped[List["Voter"]] = \
        relationship(back_populates="poll", cascade="all, delete-orphan")
    """
    admins = relationship()
    questions = relationship()
    voters = relationship()
    reviews = relationship()
    waitlist = relatiohship()
    redflags = relationship()
    metadata = relationship()
    notices = relationship()
    inbox = relationship()
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
