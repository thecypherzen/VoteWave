#!/usr/bin/python3

from sqlalchemy import Boolean, ForeignKey, Integer, String
from sqlalchemy.ext.associationproxy import AssociationProxy,\
    association_proxy
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.mysql import TEXT
from models.base_class import Base, BaseClass



class Redflag(BaseClass, Base):
    """Defines a waitlist class"""
    count = 0
    __tablename__ = "redflags"
    serial: Mapped[str] = mapped_column(
        Integer, nullable=False, autoincrement=True)
    poll_id: Mapped[str] = mapped_column(
        ForeignKey("polls.id"), nullable=True)
    election_id: Mapped[str] = mapped_column(
        ForeignKey("elections.id"), nullable=True)
    message_id: Mapped[str] = mapped_column(
        ForeignKey("messages.id"), nullable=False)
    is_treated: Mapped[str] = mapped_column(
        Boolean, nullable=False, default=False)

    # relationships
    election: Mapped["Election"] = relationship(back_populates="redflags")
    message: Mapped["Message"] = relationship(back_populates="redflag")
    poll: Mapped["Poll"] = relationship(back_populates="redflags")

    # association proxies
    author: AssociationProxy["Message"] = association_proxy(
        "message", "sender")
    receiver: AssociationProxy["Message"] = association_proxy(
        "message", "receiver")

    def __init__(self, *args, **kwargs):
        """Initialises a the candidate class"""
        from models import storage

        if kwargs and (message := kwargs.get("message")):
            # validate message and attributes
            if not message:
                return
            # validate reciver/sender types
            rtype = message.receiver_type.lower()
            stype = message.sender_type.lower()
            if not any([rtype == "poll", rtype == "election",
                    stype == "voter", stype == "candidate"]):
                return
            # fetch receiving poll/election object
            recvr = storage.get(rtype.capitalize(), message.receiver_id)
            if not recvr:
                return

            # set other attributes and init
            self.message_id = message.id
            if rtype == "election":
                self.election_id = recvr.id
            else:
                self.poll_id = recvr.id

            self.is_treated = False

            # save message as it's required for redflag
            storage.add(message)
            storage.save()
            super().__init__()


    def treat(self):
        """Updates a redflag's status to treated"""
        self.is_treated = True
        self.save()
