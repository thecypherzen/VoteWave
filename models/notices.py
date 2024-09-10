#!/usr/bin/python3

from datetime import datetime, timedelta
from sqlalchemy import DateTime, Integer, String
from sqlalchemy.dialects.mysql import TEXT
from sqlalchemy.orm import Mapped, mapped_column
from models.base_class import Base, BaseClass


class Notice(BaseClass, Base):
    """Defines a notice class"""
    count = 0
    __tablename__ = "notices"
    serial: Mapped[int] = mapped_column(
        Integer, nullable=False, autoincrement=True)
    owner_id: Mapped[str] = mapped_column(String(32), nullable=True)
    owner_type: Mapped[str] = mapped_column(String(32), nullable=True)
    subject: Mapped[str] = mapped_column(String(255), nullable=False)
    body: Mapped[str] = mapped_column(TEXT, nullable=False)
    expires: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    def __init__(self, *args, **kwargs):
        """Initialises  of a notice"""
        items = ["owner_id", "owner_type", "subject", "body"]
        if kwargs and all(key in items for key in kwargs.keys()):
            self.expires = kwargs.get("expires") or\
                datetime.now() + timedelta(days=7)
            if kwargs.get("expires"):
                del kwargs["expires"]
            super().__init__(*args, **kwargs)
