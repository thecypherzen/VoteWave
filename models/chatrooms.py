#!/usr/bin/python3
"""defines the user class"""


from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import LONGTEXT
from models.base_class import Base, BaseClass


class Chatroom(BaseClass, Base):
    count = 0

    """Defines a user class"""
    __tablename__ = "chatrooms"
    serial: Mapped[int] = mapped_column(Integer, nullable=False,
                                        autoincrement=True)
    poll_id: Mapped[str] = mapped_column(String(32), nullable=False)
    election_id: Mapped[str] = mapped_column(String(32), nullable=False)
    code: Mapped[str] = mapped_column(String(32), nullable=False)
    is_open: Mapped[str] = mapped_column(Boolean, nullable=False)
    history: Mapped[str] = mapped_column(LONGTEXT, nullable=False)

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
