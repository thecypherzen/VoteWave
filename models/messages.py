#!/usr/bin/python3

from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.base_class import Base, BaseClass
from typing import List

"""
message_metadata = Table(
    "message_metadata", Base.metadata,
    Column(ForeignKey("messages.id"), primary_key=True,
           ondelete="CASCADE", onupdate="CASCADE"),
    Column(ForeignKey("metadata.id"), primary_key=True,
           ondelete="CASCADE", onupdate="CASCADE")
)
"""
class MessageInbox(BaseClass, Base):
    count = 0
    __tablename__ = "message_inbox"
    serial: Mapped[int] = mapped_column(
        Integer, nullable=False)
    message_id: Mapped[str] = mapped_column(
        ForeignKey("messages.id"), primary_key=True)
    inbox_id: Mapped[str] = mapped_column(
        ForeignKey("inboxes.id"), primary_key=True)

    # relationships
    inbox: Mapped["Inbox"] = relationship(
        back_populates="message_items")
    message: Mapped["Message"] = relationship(
        back_populates="inbox_items")



class Message(BaseClass, Base):
    """Defines a message class"""
    count = 0
    __tablename__ = "messages"
    serial: Mapped[int] = mapped_column(
        Integer, nullable=False, autoincrement=True)
    content: Mapped[str] = mapped_column(LONGTEXT, nullable=False)

    # relationships
    inbox_items: Mapped["MessageInbox"] = relationship(
        back_populates="message", cascade="all, delete-orphan")
    inboxes = association_proxy("inbox_items", "inbox")
    #_metadata: Mapped[List["Metadata"]] = relationship(
    #   secondary="message_metadata", back_populates="message")

    def __init__(self, *args, **kwargs):
        """Initialises a message instance"""
        if kwargs and kwargs.get("content"):
            super().__init__(*args, **kwargs)
