#!/usr/bin/python3

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from models.base_class import Base, BaseClass


class Candidate(BaseClass, Base):
    """Defines a Candidate class"""
    __count = 0
    __tablename__ = "candidates"
    serial: Mapped[str] = \
        mapped_column(Integer, nullable=False, autoincrement=True)
    election_id: Mapped[str] = mapped_column(String(32), nullable=False)
    user_id: Mapped[str] = mapped_column(String(32), nullable=False)
    party_name: Mapped[str] = mapped_column(String(128), nullable=False)
    party_initials: Mapped[str] = mapped_column(String(10), nullable=False)
    votes: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    """
    reviews = relationship()
    redflags = relationship()
    messages = relationship()
    metadata = relationship()
    """

    def __init__(self, *args, **kwargs):
        """Initialises a the candidate class"""
        if kwargs and all([kwargs.get("election_id"), kwargs.get("user_id")]):
            self.election_id = kwargs["election_id"]
            self.user_id = kwargs["user_id"]
            self.party_name = kwargs.get("party_name") or \
                f"Unamed Party-{self.__count + 1}"
            self.party_initials = kwargs.get("party_initials") or ""
            super().__init__()
            Candidate.__count += 1

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
