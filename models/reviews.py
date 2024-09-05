#!/usr/bin/python3

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.base_class import Base, BaseClass
from typing import List


class Review(BaseClass, Base):
    """Defines a waitlist class"""
    count = 0
    __tablename__ = "reviews"
    serial: Mapped[str] = \
        mapped_column(Integer, nullable=False, autoincrement=True)
    user_id: Mapped[str] = \
        mapped_column(ForeignKey("users.id"), nullable=True)
    voter_id: Mapped[str] = \
        mapped_column(ForeignKey("voters.id"), nullable=True)
    candidate_id: Mapped[str] = \
        mapped_column(ForeignKey("candidates.id"), nullable=True)
    poll_id: Mapped[str] = \
        mapped_column(ForeignKey("polls.id"), nullable=True)
    election_id: Mapped[str] = \
        mapped_column(ForeignKey("elections.id"), nullable=True)
    stars: Mapped[str] = mapped_column(Integer, nullable=False)
    message: Mapped[str] = \
        mapped_column(String(255), nullable=False, default="")

    # relationships
    poll: Mapped["Poll"] = relationship(back_populates="reviews")
    election: Mapped["Election"] = relationship(back_populates="reviews")
    user: Mapped["User"] = relationship(back_populates="reviews")
    voter: Mapped["Voter"] = relationship(back_populates="reviews")
    candidate: Mapped["Candidate"] = relationship(back_populates="reviews")


    def __init__(self, *args, **kwargs):
        """Initialises a the candidate class"""
        if kwargs and kwargs.get("stars") and \
           any([kwargs.get("user_id"), kwargs.get("voter_id"),
                kwargs.get("candidate_id")]) and \
                any([kwargs.get("poll_id"), kwargs.get("election_id")]):
            super().__init__(*args, **kwargs)
