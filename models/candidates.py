#!/usr/bin/python3

from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.base_class import Base, BaseClass
from typing import List


class Candidate(BaseClass, Base):
    """Defines a Candidate class"""
    count = 0
    __tablename__ = "candidates"
    serial: Mapped[str] = mapped_column(
        Integer, nullable=False, autoincrement=True)
    election_id: Mapped[str] = mapped_column(
        ForeignKey("elections.id"), nullable=False)
    user_id: Mapped[str] = mapped_column(
        ForeignKey("users.id"), nullable=False)
    party_name: Mapped[str] = mapped_column(String(128), nullable=False)
    party_initials: Mapped[str] = mapped_column(String(10), nullable=False)
    votes: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    manifesto: Mapped[str] = mapped_column(LONGTEXT, nullable=False)
    election: Mapped["Election"] = relationship(back_populates="candidates")
    reviews: Mapped[List["Review"]] = relationship(
        back_populates="candidate", cascade="all, delete-orphan")

    # relationships
    _metadata: Mapped[List["Metadata"]] = relationship(
        primaryjoin="and_(Metadata.owner_id == Candidate.id, \
        Metadata.owner_type == 'candidate')",
        foreign_keys="Metadata.owner_id",
        overlaps="_metadata, _metadata, _metadata")

    """
    redflags = relationship()
    """

    def __init__(self, *args, **kwargs):
        """Initialises a the candidate class"""
        if kwargs and all([kwargs.get("election_id"), kwargs.get("user_id")]):
            self.election_id = kwargs["election_id"]
            self.user_id = kwargs["user_id"]
            self.party_name = kwargs.get("party_name") or \
                f"Unamed Party-{self.random_string(24)}"
            self.party_initials = kwargs.get("party_initials") or ""
            self.manifesto = kwargs.get("manifesto") or ""
            super().__init__()

    def raise_redflag(self, message, metadata=None):
        """raises a redflag about an election
        Destination is election inbox
        Returns: True on success, False otherwise
        """

    def send_message(self, content=None):
        """sends a message to a receiver. Only text content is supported
        Destination is election inbox

        Returns: True on success, False otherwise
        """
        pass

    def submit_review(self, stars, message=None):
        """Submits a review rating for on election
        Returns: True on success, False otherwise
        """
        pass
