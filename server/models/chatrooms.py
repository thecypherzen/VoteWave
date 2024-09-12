#!/usr/bin/python3
"""defines the user class"""


from sqlalchemy import Boolean, ForeignKey, Integer, String,\
    UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.mysql import LONGTEXT
from models.base_class import Base, BaseClass
from typing import Optional


class Chatroom(BaseClass, Base):
    count = 0

    """Defines a user class"""
    __tablename__ = "chatrooms"
    serial: Mapped[int] = mapped_column(Integer, nullable=False,
                                        autoincrement=True)
    poll_id: Mapped[str] = \
        mapped_column(ForeignKey("polls.id"), nullable=True)
    election_id: Mapped[str] = \
        mapped_column(ForeignKey("elections.id"), nullable=True)
    code: Mapped[str] = mapped_column(String(32), nullable=False)
    is_open: Mapped[str] = mapped_column(Boolean, nullable=False)
    history: Mapped[str] = mapped_column(LONGTEXT, nullable=False)
    election: Mapped[Optional["Election"]] = relationship(back_populates="chatroom")
    poll: Mapped[Optional["Poll"]] = relationship(back_populates="chatroom")

    __table_args__ = (UniqueConstraint("poll_id", "election_id", "id"),)

    def __init__(self, *args, **kwargs):
        """Initialize user class"""
        to_delete = ["history", "is_open", "code"]
        if any([kwargs.get("election_id"), kwargs.get("poll_id")]):
            self.code = Chatroom.random_string()
            self.history = kwargs.get("history") or ""
            self.is_open = kwargs.get("is_open") or False
            for item in to_delete:
                if kwargs.get(item):
                    del kwargs[item]
            super().__init__(*args, **kwargs)
