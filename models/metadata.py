#!/usr/bin/python3

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from models.base_class import Base, BaseClass


class Metadata(BaseClass, Base):
    """Defines a blacklist class"""
    __count = 0
    __tablename__ = "metadata"
    serial: Mapped[str] = \
        mapped_column(Integer, nullable=False, autoincrement=True)
    election_id: Mapped[str] = mapped_column(String(32), nullable=False)
    user_id: Mapped[str] = mapped_column(String(32), nullable=True)
    poll_id: Mapped[str] = mapped_column(String(32), nullable=True)
    chatroom_id: Mapped[str] = mapped_column(String(32), nullable=True)
    candidate_id: Mapped[str] = mapped_column(String(32), nullable=True)
    redflag_id: Mapped[str] = mapped_column(String(32), nullable=True)
    option_id: Mapped[str] = mapped_column(String(32), nullable=True)
    voter_id: Mapped[str] = mapped_column(String(32), nullable=True)
    location: Mapped[str] = \
        mapped_column(String(255), nullable=False, default="")
    name: Mapped[str] = mapped_column(String(128), nullable=False)
    use_as: Mapped[str] = mapped_column(String(20), nullable=False)
    mime_type: Mapped[str] = mapped_column(String(20), nullable=False)

    def __init__(self, *args, **kwargs):
        """Initialises a the candidate class"""
        items = ["election_id", "user_id", "poll_id", "candidate_id",
                 "redflag_id", "voter_id", "Option_id", "chatroom_id"]
        if kwargs and \
           all([name := kwargs.get("name"),
                use_as := kwargs.get("use_as"),
                mime_type := kwargs.get("mime_type")]) and \
                any(key in items for key in kwargs.keys()):
            super().__init__(*args, **kwargs)
            Metadata.__count += 1
