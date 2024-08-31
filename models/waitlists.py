#!/usr/bin/python3

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from models.base_class import Base, BaseClass


class Waitlist(BaseClass, Base):
    """Defines a waitlist class"""
    __count = 0
    __tablename__ = "waitlists"
    serial: Mapped[str] = \
        mapped_column(Integer, nullable=False, autoincrement=True)
    user_id: Mapped[str] = mapped_column(String(32), nullable=True)
    poll_id: Mapped[str] = mapped_column(String(32), nullable=True)
    election_id: Mapped[str] = mapped_column(String(32), nullable=True)
    join_as: Mapped[str] = mapped_column(String(10), nullable=False)
    """
    polls = relationship()
    elections = relationship()
    users = relationship()
    """

    def __init__(self, *args, **kwargs):
        """Initialises a the candidate class"""
        if kwargs and kwargs.get("join_as"):
            self.election_id = kwargs.get("election_id")
            self.user_id = kwargs.get("user_id")
            self.poll_id = kwargs.get("poll_id")
            self.join_as = kwargs.get("join_as")
            super().__init__()
            Waitlist.__count += 1

    def all(self):
        """returns list of all users on the waitlist for either
        an election or poll

        Returns: a list  users on each waitlist on success or an
          empty list if none.
        """
        pass
