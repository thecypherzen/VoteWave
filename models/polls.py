#!/urs/bin/python3
"""defines the base activity from which polls and
    elections will inherit
"""

from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date, datetime
from models.base_activity import BaseActivity


class Poll(BaseActivity):
    """Defines a user class

    """
    __count = 0
    serial: Mapped[int] = mapped_column(Integer, nullable=False, autoincrement=True)
    location: Mapped[str] = mapped_column(String(255), nullable=False)
    title: Mapped[str] = mapped_column(String(128), nullable=False)
    allows_anonymous: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    allow_multi_votes: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
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
        """Initialize user class"""
        if all([kwargs.get("starts_at"), kwargs.get("ends_at"), kwargs.get("security_key")]):
            if (title := kwargs.get("title")):
                self.title = title
                del kwargs["title"]
            else:
                self.title = f"Poll-{Election.__count + 1}"
            self.location = "votewave/user_id/polls/poll_id"

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
