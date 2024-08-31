#!/usr/bin/python3

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from models.base_class import Base, BaseClass


class Blacklist(BaseClass, Base):
    """Defines a blacklist class"""
    __count = 0
    __tablename__ = "blacklists"
    serial: Mapped[str] = \
        mapped_column(Integer, nullable=False, autoincrement=True)
    blocked_user_id: Mapped[str] = mapped_column(String(32), nullable=False)
    user_id: Mapped[str] = mapped_column(String(32), nullable=True)
    poll_id: Mapped[str] = mapped_column(String(32), nullable=True)
    election_id: Mapped[str] = mapped_column(String(32), nullable=True)
    reason: Mapped[str] = mapped_column(String(128), nullable=False)
    """
    polls = relationship()
    elections = relationship()
    users = relationship()
    """

    def __init__(self, *args, **kwargs):
        """Initialises a the candidate class"""
        if kwargs and all([kwargs.get("reason"),
                           kwargs.get("blocked_user_id")]):
            self.blocked_user_id = kwargs.get("blocked_user_id")
            self.election_id = kwargs.get("election_id")
            self.user_id = kwargs.get("user_id")
            self.poll_id = kwargs.get("poll_id")
            self.reason = kwargs.get("reason")
            super().__init__()
            Waitlist.__count += 1
