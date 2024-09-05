#!/usr/bin/python3

from datetime import datetime, timedelta
from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from models.base_class import Base, BaseClass


class Notice(BaseClass, Base):
    """Defines a blacklist class"""
    count = 0
    __tablename__ = "notices"
    serial: Mapped[str] = \
        mapped_column(Integer, nullable=False, autoincrement=True)
    election_id: Mapped[str] = mapped_column(String(32), nullable=True)
    poll_id: Mapped[str] = mapped_column(String(32), nullable=True)
    message: Mapped[str] = mapped_column(String(255), nullable=False)
    expires: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    def __init__(self, *args, **kwargs):
        """Initialises a the candidate class"""
        items = ["election_id", "poll_id"]
        if kwargs and kwargs.get("message") and \
           any(key in items for key in kwargs.keys()):
            self.expires = kwargs.get("expires") or\
                datetime.now() + timedelta(weeks=10800)
            if kwargs.get("expires"):
                del kwargs["expires"]
            super().__init__(*args, **kwargs)
