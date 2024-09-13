#!/usr/bin/python3

from sqlalchemy import Column, CheckConstraint, ForeignKey, \
    Integer, String, Table, UniqueConstraint
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.ext.associationproxy import association_proxy,\
    AssociationProxy
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.base_class import Base, BaseClass
from typing import List


# message_inbox bridge table
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

# message_metadata bridge table
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


# message table itself
class Message(BaseClass, Base):
    """Defines a message class"""
    count = 0
    __tablename__ = "messages"
    serial: Mapped[int] = mapped_column(
        Integer, nullable=False, autoincrement=True)
    sender_id: Mapped[str] = mapped_column(
        String(32), nullable=False)
    sender_type: Mapped[str] = mapped_column(
        String(16), nullable=False)
    receiver_id: Mapped[str] = mapped_column(
        String(32), nullable=False)
    receiver_type: Mapped[str] = mapped_column(
        String(16), nullable=False)
    admin_id: Mapped[str]  = mapped_column(
        String(32), nullable=True)
    subject: Mapped[str] = mapped_column(String(255), nullable=False)
    body: Mapped[str] = mapped_column(LONGTEXT, nullable=False)

    # relationships
    c_receiver: Mapped["Candidate"] = relationship(
        primaryjoin="and_(Message.receiver_id == Candidate.id, \
        Message.receiver_type == 'candidate')", foreign_keys=[receiver_id],
        overlaps="sent_messages, sent_messages, v_sender")
    c_sender: Mapped["Candidate"] = relationship(
        primaryjoin="and_(Message.sender_id == Candidate.id, \
        Message.sender_type == 'candidate')", foreign_keys=[sender_id],
        overlaps="sent_messages, sent_messages, v_sender")
    e_receiver: Mapped["Election"] = relationship(
        primaryjoin="and_(Message.receiver_id == Election.id, \
        Message.receiver_type == 'election')",
        foreign_keys=[receiver_id], overlaps="poll, c_receiver")
    e_sender: Mapped["Election"] = relationship(
        primaryjoin="and_(Message.sender_id == Election.id, \
        Message.sender_type == 'election')", foreign_keys=[sender_id],
        overlaps="c_sender, p_sender, v_sender, sent_messages, sent_messages")
    inbox_items: Mapped[List[MessageInbox]] = relationship(
        back_populates="message", cascade="all, delete-orphan")
    mdata_items: Mapped[List[MessageMetadata]] = relationship(
        back_populates="message", cascade="all, delete-orphan",)
    p_receiver: Mapped["Poll"] = relationship(
        primaryjoin="and_(Message.receiver_id == Poll.id, \
        Message.receiver_type == 'poll')", foreign_keys=[receiver_id],
        overlaps="c_receiver")
    p_sender: Mapped["Poll"] = relationship(
        primaryjoin="and_(Message.sender_id == Poll.id, \
        Message.sender_type == 'poll')", foreign_keys=[sender_id],
        overlaps="c_sender, e_sender, v_sender, sent_messages")
    redflag: Mapped["Redflag"] = relationship(back_populates="message")
    v_receiver: Mapped["Voter"] = relationship(
        primaryjoin="and_(Message.receiver_id == Voter.id, \
        Message.receiver_type == 'voter')", foreign_keys=[receiver_id],
        overlaps="e_receiver, p_receiver, c_receiver")
    v_sender: Mapped["Voter"] = relationship(
        primaryjoin="and_(Message.sender_id == Voter.id, \
        Message.sender_type == 'voter')", foreign_keys=[sender_id],
        overlaps="sent_messages, sent_mesages")

    # association proxies
    inboxes: AssociationProxy[List["Inbox"]] = association_proxy(
        "inbox_items", "inbox")
    _metadata: AssociationProxy[List["Metadata"]] = association_proxy(
        "mdata_items", "mdata",
        creator=lambda data :MessageMetadata(mdata=data))

    def __init__(self, *args, **kwargs):
        """Initialises a message instance"""
        if kwargs and \
           all([kwargs.get("body"), kwargs.get("sender_id"),
                kwargs.get("sender_type"), kwargs.get("subject"),
                kwargs.get("receiver_type"),
                kwargs.get("receiver_id")]):
            self.subject = kwargs.get("subject") or \
                f"Message-{self.random_string(16)}"
            super().__init__(*args, **kwargs)

    @property
    def receiver(self):
        """Returns the receiver of a message"""
        if self.c_receiver:
            return self.c_receiver
        elif self.e_receiver:
            return self.e_receiver
        elif self.p_receiver:
            return self.p_receiver
        else:
            return self.v_receiver


    @property
    def sender(self):
        """Returns the sender of a message"""
        if self.c_sender:
            return self.c_sender
        elif self.e_sender:
            return self.e_sender
        elif self.p_receiver:
            return self.p_sender
        else:
            return self.v_sender


    def add_metadata(self, *metadata):
        """Associates given metadata to a message instance"""
        for meta_item in metadata:
            if isinstance(metadata, list):
                for item in meta_item:
                    if item not in self.__metadata:
                        self._metadata.append(item)
            else:
                if meta_item not in self._metadata:
                    self._metadata.append(meta_item)
        self.save()

    def remove_metadata(self, *metadata):
        """Dissociates given metadata with message instance"""
        for meta_item in metadata:
            if isinstance(meta_item, list):
                for item in meta_item:
                    if item in self.mdata:
                        self._metadata.remove(item)
            else:
                if meta_item in self.mdata:
                    self._metadata.remove(meta_item)
        self.save()

    def send(self):
        """Sends a message instance the receiver"""
        from models import storage

        res = {f"{self.serial}":
               {"success": False, "error": "Receiver doesn't exist"}
               }
        # fetch receiver's object
        receiver_name = self.receiver_type.capitalize()
        receiver_obj = storage.get(receiver_name, self.receiver_id)
        if not receiver_obj:
            return res

        # get receiver's inbox
        if any([receiver_name == "Election",
                receiver_name == "Poll"]):
            inbox = receiver_obj.inbox
        elif any([receiver_name == "Candidate",
                  receiver_name == "Voter"]):
            user = storage.get("User", receiver_obj.user_id)
            if not user:
                return res
            inbox = user.inbox
        else:
            return res

        # send message
        res = inbox.add_message(self)
        return res


"""
# message_sender bridge table
class MessageSender(BaseClass, Base):
    # Associates a message with a sender, which
    # could be a user, poll or an election
    #
    __tablename__ = "message_sender"
    count = 0
    serial: Mapped[int] = mapped_column(
        Integer, nullable=False, autoincrement=True)
    user_id: Mapped[str] = mapped_column(
        ForeignKey("users.id"), nullable=True)
    poll_id: Mapped[str] = mapped_column(
        ForeignKey("polls.id"), nullable=True)
    election_id: Mapped[str] = mapped_column(
        ForeignKey("elections.id"), nullable=True)
   message_id: Mapped[str] = mapped_column(
        ForeignKey("messages.id"), primary_key=True)
    sender_type: Mapped[str] = mapped_column(
        String(16), nullable=False)

    # relationships
    election: Mapped["Election"] = relationship(
        back_populates="msg_sndr_items")
    poll: Mapped["Poll"] = relationship(
        back_populates="msg_sndr_items")
    user: Mapped["User"] = relationship(
        back_populates="msg_sndr_items")
    message: Mapped[List["Message"]] = relationship(
        back_populates="sent_message")

    # mapper configuration
    __table_args__ = (
        CheckConstraint(
            "user_id IS NOT NULL AND poll_id IS NULL AND \
            election_id IS NULL OR " "user_id IS NULL AND \
            poll_id IS NOT NULL AND election_id IS NULL OR "
        "user_id IS NULL AND poll_id IS NULL AND election_id \
        IS NOT NULL", name="only1sender_constt"),
        UniqueConstraint("message_id", 'user_id', 'poll_id', \
                         'election_id'))
    __mapper_args__ = { "polymorphic_on": sender_type }

    @property
    def sender(self):
        # Returns the sender of a message
        if self.sender_type == "election":
            return self.election
        elif self.sender_type == "user":
            return self.user
        else:
            return self.poll
"""

 
