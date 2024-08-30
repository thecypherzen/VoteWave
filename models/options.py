#!/usr/bin/python3
"""defines the user class"""


from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from models.base_class import Base, BaseClass


class Option(BaseClass, Base):
    __count = 0

    """Defines a user class"""
    __tablename__ = "options"
    serial: Mapped[int] = mapped_column(Integer, nullable=False,
                                        autoincrement=True)
    question_id: Mapped[str] = mapped_column(String(32), nullable=False)
    value: Mapped[str] = mapped_column(String(255), nullable=False)
    votes: Mapped[str] = mapped_column(Integer, nullable=False, default=0)

    def __init__(self, *args, **kwargs):
        """Initialize user class"""
        if all([kwargs.get('question_id'), kwargs.get("value")]):
            to_delete = ["question_id", "votes", "serial", "value"]
            self.serial = Option.__count + 1
            self.question_id = kwargs.get("question_id")
            self.value = kwargs.get("value")
            self.votes = 0
            for item in to_delete:
                if kwargs.get(item):
                    del kwargs[item]
            super().__init__(*args, **kwargs)
            Option.__count += 1
