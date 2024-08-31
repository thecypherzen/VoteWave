#!/usr/bin/python3

from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from models.base_class import Base, BaseClass


class Voter(BaseClass, Base):
    """Defines an admin class"""
    __count = 0
    __tablename__ = "voters"
    serial: Mapped[str] = \
        mapped_column(Integer, nullable=False, autoincrement=True)
    user_id: Mapped[str] = mapped_column(String(32), nullable=False)
    election_id: Mapped[str] = mapped_column(String(32), nullable=True)
    poll_id: Mapped[str] = mapped_column(String(32), nullable=True)
    has_voted: Mapped[bool] = \
        mapped_column(Boolean, nullable=False, default=False)
    """
    elections = relationship()
    polls = relationship()
    reviews = relationship()
    red_flags = relationship()
    """

    def __init__(self, *args, **kwargs):
        """Initialises a the candidate class"""
        if kwargs and kwargs.get("user_id") and \
           any([kwargs.get("election_id"), kwargs.get("poll_id")]):
            self.serial = Voter.__count + 1
            self.user_id = kwargs.get("user_id")
            self.election_id = kwargs.get("election_id")
            self.poll_id = kwargs.get("poll_id")
            self.has_voted = False
            super().__init__()
            Voter.__count += 1
