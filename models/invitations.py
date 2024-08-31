#!/usr/bin/python3
"""defines the user class"""


from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from models.base_class import Base, BaseClass


class Invitation(BaseClass, Base):
    count = 0

    """Defines a user class"""
    __tablename__ = "invitations"
    serial: Mapped[int] = mapped_column(Integer, nullable=False,
                                        autoincrement=True)
    user_from: Mapped[str] = mapped_column(String(32), nullable=False)
    user_to: Mapped[str] = mapped_column(String(32), nullable=False)
    link: Mapped[str] = mapped_column(String(255), nullable=False)

    def __init__(self, *args, **kwargs):
        """Initialize user class"""
        if kwargs and all([user_from := kwargs.get('user_from'),
                           user_to := kwargs.get("user_to"),
                           link := kwargs.get("link")]):
            self.user_from = user_from
            self.user_to = user_to
            self.link = link
            super().__init__()
