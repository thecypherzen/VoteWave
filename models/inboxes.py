#!/usr/bin/python3
from sqlalchemy import Column, ForeignKey, Integer, String,\
    Table, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.base_class import Base, BaseClass
from typing import List


class Inbox(BaseClass, Base):
    """Defines an inbox class"""
    count = 0
    __tablename__ = "inboxes"
    serial: Mapped[str] = \
        mapped_column(Integer, nullable=False, autoincrement=True)
    owner_id: Mapped[str] = mapped_column(String(32), nullable=True)
    owner_type: Mapped[str] = mapped_column(String(32), nullable=True)
    __table_args__ = (UniqueConstraint("owner_id", "owner_type"),)

    # relationships
    messages: Mapped[List["Message"]] = relationship(
        back_populates="inbox", cascade="all, delete-orphan")
    user: Mapped["User"] = relationship(
        back_populates="inbox", foreign_keys="Inbox.owner_id",
        primaryjoin="and_(Inbox.owner_id == User.id, \
        Inbox.owner_type == 'user')", overlaps="inbox, election, poll"
    )
    election: Mapped["Election"] = relationship(
        back_populates="inbox", foreign_keys="Inbox.owner_id",
        primaryjoin="and_(Inbox.owner_id == Election.id, \
        Inbox.owner_type == 'election')", overlaps="user, inbox, poll"
    )
    poll: Mapped["Poll"] = relationship(
        back_populates="inbox", foreign_keys="Inbox.owner_id",
        primaryjoin="and_(Inbox.owner_id == Poll.id, \
        Inbox.owner_type == 'poll')", overlaps="inbox, user, election"
    )

    def __init__(self, *args, **kwargs):
        """Initialises an inbox instance"""
        items = ["owner_id", "owner_type"]
        if kwargs and all([kwargs.get("owner_id"),
                           kwargs.get("owner_type")]):
            super().__init__(*args, **kwargs)
