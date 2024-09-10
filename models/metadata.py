#!/usr/bin/python3

from sqlalchemy import Integer, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.associationproxy import association_proxy
from models.base_class import Base, BaseClass


class Metadata(BaseClass, Base):
    """Defines a blacklist class"""
    count = 0
    __tablename__ = "metadata"
    serial: Mapped[str] = mapped_column(
        Integer, nullable=False, autoincrement=True)
    name: Mapped[str] = mapped_column(String(128), nullable=False)
    location: Mapped[str] = mapped_column(
        String(255), nullable=False, default="")
    owner_id: Mapped[str] = mapped_column(String(32), nullable=False)
    owner_type: Mapped[str] = mapped_column(String(16), nullable=False)
    use_as: Mapped[str] = mapped_column(String(20), nullable=False)
    mime_type: Mapped[str] = mapped_column(String(20), nullable=False)

    __table_args__ = (
        UniqueConstraint("name", "location", "owner_id", "use_as",
                         "mime_type", name="metadata_uq"),)

    # relationships
    election: Mapped["Election"] = relationship(
        back_populates="_metadata",
        primaryjoin="and_(Metadata.owner_id == Election.id, \
        Metadata.owner_type == 'election')",
        overlaps="_metadata, user, notice",
        foreign_keys="Metadata.owner_id")
    candidate: Mapped["Candidate"] = relationship(
        back_populates="_metadata", foreign_keys="Metadata.owner_id",
        overlaps="_metadata, election, poll, user, notice",
        primaryjoin="and_(Metadata.owner_id == Candidate.id, \
        Metadata.owner_type == 'candidate')")
    message_items: Mapped["MessageMetadata"] = relationship(
        back_populates="mdata", cascade="all, delete-orphan")
    messages = association_proxy("message_items", "message")
    notice: Mapped["Notice"] = relationship(
        primary_join="and_(Metadata.owner_id == 'Notice.owner_id', \
        Metadata.owner_type == 'notice')", back_populates="meta_data",
        overlaps="election, candidate, poll, user, meta_data")
    poll: Mapped["Poll"] = relationship(
        back_populates="_metadata", foreign_keys="Metadata.owner_id",
        overlaps="_metadata, election, user, candidate, notice",
        primaryjoin="and_(Metadata.owner_id == Poll.id, \
        Metadata.owner_type == 'poll')")
    user: Mapped["User"] = relationship(
        back_populates="_metadata", foreign_keys="Metadata.owner_id",
        primaryjoin="and_(Metadata.owner_id == User.id, \
        Metadata.owner_type == 'user')",
        overlaps="_metadata, election, candidate, notice, poll")


    def __init__(self, *args, **kwargs):
        """Initialises a the candidate class"""
        args = ["name", "use_as", "mime_type", "location",
                  "owner_id", "owner_type"]
        if kwargs and all([kwargs.get(arg) for arg in args]):
            super().__init__(*args, **kwargs)
