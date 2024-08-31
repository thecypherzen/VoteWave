#!/usr/bin/python3

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from models.base_class import Base, BaseClass


class Admin(BaseClass, Base):
    """Defines an admin class"""
    __count = 0
    __tablename__ = "admins"
    serial: Mapped[str] = \
        mapped_column(Integer, nullable=False, autoincrement=True)
    user_id: Mapped[str] = mapped_column(String(32), nullable=False)
    election_id: Mapped[str] = mapped_column(String(32), nullable=True)
    poll_id: Mapped[str] = mapped_column(String(32), nullable=True)
    """
    elections = relationship()
    polls = relationship()
    users = relationship()
    """

    def __init__(self, *args, **kwargs):
        """Initialises a the candidate class"""
        if kwargs and kwargs.get("user_id") and \
           any([kwargs.get("election_id"), kwargs.get("poll_id")]):
            self.user_id = kwargs.get("user_id")
            self.election_id = kwargs.get("election_id")
            self.poll_id = kwargs.get("poll_id")
            super().__init__()
            Admin.__count += 1

    def send_message(self, message=None):
        """sends a message to activity participants only.
        Destination is the user's inbox. Message content is a dict
        + in the format: {"body": "<body>", "metadata": ["<metadata>"]}

        Returns: True on success, False otherwise
        """
        pass

    def post_notice(self, message=None):
        """Posts a notice to the event's notice board
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
