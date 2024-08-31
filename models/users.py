#!/usr/bin/python3
"""defines the user class"""


from sqlalchemy import Date, DateTime, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from uuid import uuid4
from datetime import date, datetime
from flask_login import UserMixin
import models

Base = models.base_class.Base
BaseClass = models.base_class.BaseClass

format = "%Y-%m-%dT%H:%M:%S.%f"

class User(UserMixin, BaseClass, Base):
    """Defines a user class"""
    __count = 0
    __tablename__ = "users"
    serial: Mapped[int] = mapped_column(Integer, nullable=False,
                                        autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = \
        mapped_column(String(50), nullable=False, default="")
    email: Mapped[str] = mapped_column(String(50), nullable=False)
    security_key: Mapped[str] = mapped_column(String(128), nullable=False)
    passwd_hash: Mapped[str] = mapped_column(String(128), nullable=False)
    salt: Mapped[str] = mapped_column(String(16), nullable=False)
    username: Mapped[str] = mapped_column(String(30), nullable=False)
    phone: Mapped[str] = mapped_column(String(15), nullable=False, default="")
    prefix: Mapped[str] = mapped_column(String(10), nullable=True,
                                        default="")
    location: Mapped[str] = mapped_column(String(255), nullable=False)
    dob: Mapped[date] = mapped_column(Date, nullable=False)
    address: Mapped[str] = \
        mapped_column(String(255), nullable=False, default="")
    """
    elections = relationship()
    polls = relationship()
    invitations = relationship()
    reviews = relationship()
    metadata = relationship()
    blacklist = relationship()
    inbox = relationship()
    """

    def __init__(self, *args, **kwargs):
        """Initialize user class"""
        if all([kwargs.get("first_name"), kwargs.get("password"),
                kwargs.get("security_key"), kwargs.get("email"),
                kwargs.get("dob")]):
            User.__count += 1

            to_delete = ["security_key", "username", "password", "dob"]
            self.serial = User.get_serial(self, User.__count)
            self.salt = User.generate_salt()
            self.username = kwargs.get("username") or f"User-{self.serial}"
            self.passwd_hash = User.generate_hash(text=kwargs["password"],
                                                  salt=self.salt)
            self.security_key = User.generate_hash(text=kwargs["security_key"],
                                                   salt=self.salt)
            self.location = kwargs.get("location") or ""
            self.dob = date.fromisoformat(kwargs.get("dob"))
            for item in to_delete:
                if kwargs.get(item):
                    del kwargs[item]
            super().__init__(*args, **kwargs)

    def send_message(self, content, receiver_id, receiver_type="user"):
        """sends a message to a receiver.

        Receivers could be anyone at all.
        """
        pass
