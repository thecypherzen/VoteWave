#!/usr/bin/python3

from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import TEXT
from models.base_class import Base, BaseClass


class Redflag(BaseClass, Base):
    """Defines a waitlist class"""
    __count = 0
    __tablename__ = "redflags"
    serial: Mapped[str] = \
        mapped_column(Integer, nullable=False, autoincrement=True)
    raised_by: Mapped[str] = mapped_column(String(32), nullable=False)
    poll_id: Mapped[str] = mapped_column(String(32), nullable=True)
    election_id: Mapped[str] = mapped_column(String(32), nullable=True)
    message: Mapped[str] = mapped_column(TEXT, nullable=False)
    is_treated: Mapped[str] = \
        mapped_column(Boolean, nullable=False, default=False)
    """
    polls = relationship()
    elections = relationship()
    """

    def __init__(self, *args, **kwargs):
        """Initialises a the candidate class"""
        if kwargs and all([kwargs.get("raised_by"), kwargs.get("message")]) \
           and any([kwargs.get("poll_id"), kwargs.get("election_id")]):
            self.serial = Redflag.__count + 1
            super().__init__(*args, **kwargs)
            Redflag.__count += 1
