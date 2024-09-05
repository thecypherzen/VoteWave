#!/usr/bin/python3

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.base_class import Base, BaseClass


class Message(BaseClass, Base):
    """Defines a message class"""
    count = 0
    __tablename__ = "messages"
    serial: Mapped[str] = \
        mapped_column(Integer, nullable=False, autoincrement=True)
    inbox_id: Mapped[str] = mapped_column(ForeignKey("inboxes.id"), nullable=False)
    content: Mapped[str] = mapped_column(LONGTEXT, nullable=False)

    # relationship
    inbox: Mapped["Inbox"] = relationship(back_populates="messages")

    def __init__(self, *args, **kwargs):
        """Initialises a message instance"""
        if kwargs and kwargs.get("content"):
            super().__init__(*args, **kwargs)
