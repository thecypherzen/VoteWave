#!/usr/bin/python3

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from models.base_class import Base, BaseClass


class Review(BaseClass, Base):
    """Defines a waitlist class"""
    count = 0
    __tablename__ = "reviews"
    serial: Mapped[str] = \
        mapped_column(Integer, nullable=False, autoincrement=True)
    user_id: Mapped[str] = mapped_column(String(32), nullable=True)
    voter_id: Mapped[str] = mapped_column(String(32), nullable=True)
    candidate_id: Mapped[str] = mapped_column(String(32), nullable=True)
    poll_id: Mapped[str] = mapped_column(String(32), nullable=True)
    election_id: Mapped[str] = mapped_column(String(32), nullable=True)
    stars: Mapped[str] = mapped_column(Integer, nullable=False)
    message: Mapped[str] = \
        mapped_column(String(255), nullable=False, default="")
    """
    polls = relationship()
    elections = relationship()
    """

    def __init__(self, *args, **kwargs):
        """Initialises a the candidate class"""
        if kwargs and kwargs.get("stars") and \
           any([kwargs.get("user_id"), kwargs.get("voter_id"),
                kwargs.get("candidate_id")]) and \
                any(kwargs.get("poll_id"), kwargs.get("election_id")):
            super().__init__(*args, **kwargs)
