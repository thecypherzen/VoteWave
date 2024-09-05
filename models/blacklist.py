#!/usr/bin/python3

from sqlalchemy import ForeignKey, Integer, \
    String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.base_class import Base, BaseClass


class Blacklist(BaseClass, Base):
    """Defines a blacklist class"""
    count = 0
    __tablename__ = "blacklist"
    serial: Mapped[str] = \
        mapped_column(Integer, nullable=False, autoincrement=True)
    blocked_user_id: Mapped[str] = mapped_column(
        ForeignKey("users.id"), nullable=False)
    user_id: Mapped[str] = mapped_column(
        ForeignKey("users.id"), nullable=True)
    poll_id: Mapped[str] = mapped_column(
        ForeignKey("polls.id"), nullable=True)
    election_id: Mapped[str] = mapped_column(
        ForeignKey("elections.id"), nullable=True)
    reason: Mapped[str] = mapped_column(String(128), nullable=False)

    __table_args__ = (
        UniqueConstraint("blocked_user_id", "user_id", "poll_id",
                         "election_id"),
    )

    # relationships
    election: Mapped["Election"] = relationship(
        back_populates="blacklist_entries",
        foreign_keys="Blacklist.election_id")
    poll: Mapped["Poll"] = relationship(
        back_populates="blacklist_entries",
        foreign_keys="Blacklist.poll_id")
    user: Mapped["User"] = relationship(
        back_populates="blacklist_entries",
        foreign_keys="Blacklist.user_id")


    def __init__(self, *args, **kwargs):
        """Initialises a blacklist instance"""
        if kwargs and \
           all([kwargs.get("reason"),
                kwargs.get("blocked_user_id"),
               any([kwargs.get("user_id"), kwargs.get("poll_id"),
                    kwargs.get("election_id")])]):
            super().__init__(*args, **kwargs)
