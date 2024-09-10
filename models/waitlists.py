#!/usr/bin/python3

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.ext.associationproxy import AssociationProxy, \
    association_proxy
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.base_class import Base, BaseClass
from typing import List


class UserWaitlist(BaseClass, Base):
    """Associates users with a waitlist"""
    count = 0
    __tablename__ = "users_waitlists"
    serial: Mapped[str] = mapped_column(
        Integer, nullable=False, autoincrement=True)
    user_id: Mapped[str] = mapped_column(
        ForeignKey("users.id"), primary_key=True)
    waitlist_id: Mapped[str] = mapped_column(
        ForeignKey("waitlists.id"), primary_key=False)
    role_for: Mapped[str] = mapped_column(
        String(16), nullable=False)

    # relationships
    user: Mapped["User"] = mapped_column(
        back_populates="users_waitlists")
    waitlist: Mapped["Waitlist"] = mapped_column(
        back_populates="waitlist_users")



class Waitlist(BaseClass, Base):
    """Defines a waitlist class"""
    count = 0
    __tablename__ = "waitlists"
    serial: Mapped[str] = mapped_column(
        Integer, nullable=False, autoincrement=True)
    owner_id: Mapped[str] = mapped_column(
        ForeignKey("activities.id"), nullable=False,
        primary_key=True)

    # relationships
    activity: Mapped["Activity"] = relationship(
        back_populates="waitlist")
    waitlist_users: Mapped[List["UserWaitlist"]] = relationship(
        back_populates="waitlist")

    # association proxies
    users: AssociationProxy[List["UserWaitlist"]] = asociation_proxy(
        "waitlist_users", "user")


    def __init__(self, *args, **kwargs):
        """Initialises a the candidate class"""
        if kwargs and \
           all([kwargs.get("join_as"), kwargs.get("user_id")] \
               and any([kwargs.get("poll_id"),
                        kwargs.get("election_id")])):
            self.election_id = kwargs.get("election_id")
            self.user_id = kwargs.get("user_id")
            self.poll_id = kwargs.get("poll_id")
            self.join_as = kwargs.get("join_as")
            super().__init__()

    def all(self):
        """returns list of all users on the waitlist for either
        an election or poll

        Returns: a list  users on each waitlist on success or an
          empty list if none.
        """
        pass
