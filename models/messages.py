#!/usr/bin/python3

from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.ext.associationproxy import association_proxy,\
    AssociationProxy
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.base_class import Base, BaseClass
from typing import List


class MessageInbox(BaseClass, Base):
    """defines a message-inbox association table"""
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


class MessageMetadata(BaseClass, Base):
    """Defines a message-metadta association"""
    count = 0
    __tablename__ = "message_metadata"
    serial: Mapped[int] = mapped_column(
        Integer, nullable=False)
    message_id: Mapped[str] = mapped_column(
        ForeignKey("messages.id"), primary_key=True)
    metadata_id: Mapped[str] = mapped_column(
        ForeignKey("metadata.id"), primary_key=True)

    # relationships
    message: Mapped["Message"] = relationship(
        back_populates="mdata_items")
    mdata: Mapped["Metadata"] = relationship(
        back_populates="message_items")


class Message(BaseClass, Base):
    """Defines a message class"""
    count = 0
    __tablename__ = "messages"
    serial: Mapped[int] = mapped_column(
        Integer, nullable=False, autoincrement=True)
    content: Mapped[str] = mapped_column(LONGTEXT, nullable=False)

    # relationships
    inbox_items: Mapped[List[MessageInbox]] = relationship(
        back_populates="message", cascade="all, delete-orphan")
    mdata_items: Mapped[List[MessageMetadata]] = relationship(
        back_populates="message", cascade="all, delete-orphan",)
    inboxes: AssociationProxy[List["Inbox"]] = association_proxy(
        "inbox_items", "inbox")
    mdata: AssociationProxy[List["Metadata"]] = association_proxy(
        "mdata_items", "mdata",
        creator=lambda data:MessageMetadata(mdata=data))



    def __init__(self, *args, **kwargs):
        """Initialises a message instance"""
        if kwargs and kwargs.get("content"):
            super().__init__(*args, **kwargs)

    def add_metadata(self, *metadata):
        """Associates given metadata to a message instance"""
        for meta_item in metadata:
            if isinstance(metadata, list):
                for item in meta_item:
                    self.mdata.append(item)
            else:
                self.mdata.append(meta_item)
        self.save()

    def remove_metadata(self, *metadata):
        """Dissociates given metadata with message instance"""
        for meta_item in metadata:
            if isinstance(meta_item, list):
                for item in meta_item:
                    if item in self.mdata:
                        self.mdata.remove(item)
            else:
                if meta_item in self.mdata:
                    self.mdata.remove(meta_item)
        self.save()



