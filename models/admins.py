#!/usr/bin/python3

from sqlalchemy import Column, DateTime, \
    ForeignKey, Integer, String, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.base_class import Base, BaseClass
from models.admin_polls_elections import admin_polls_elections as ape
from typing import List


class Admin(BaseClass, Base):
    """Defines an admin class"""
    count = 0
    __tablename__ = "admins"
    serial: Mapped[str] = \
        mapped_column(Integer, nullable=False, autoincrement=True)
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"), nullable=False)
    user: Mapped["User"] = relationship(back_populates="admin_info")
    elections: Mapped[List["Election"]] = \
        relationship(back_populates="admins", overlaps="polls",
                     secondary=ape, viewonly=True)
    polls: Mapped[List["Poll"]] = \
        relationship(back_populates="admins", overlaps="elections",
                     secondary=ape, viewonly=True)

    def __init__(self, *args, **kwargs):
        """Initialises an admin instance """
        if kwargs and kwargs.get("user_id"):
            self.user_id = kwargs.get("user_id")
            super().__init__()

    def send_message(self, message=None):
        """sends a message to activity participants only.
        Destination is the user's inbox. Message content is a dict
        + in the format: {"body": "<body>", "metadata": ["<metadata>"]}

        Returns: True on success, False otherwise
        """
        pass

    def post_notice(self, message=None):
        """Posts a notice to the event's notice boar
        Returns: True on success, False otherwise
        """
        pass

    def remove_notice(self, notice_id=None):
        """Removes a notice from the event's notice board
        Returns: True on sucess, False otherwise
        """
        pass

    def update_notice(self, notice_id=None, new_message=None):
        """Replaces the current body of notice body
        with the value of <new_message>
        Returns: True on success, False otherwise
        """
        pass
