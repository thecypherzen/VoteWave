#!/usr/bin/python3
"""contains the definition of an option class"""


from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.dialects.mysql import TEXT
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.base_class import Base, BaseClass


class Option(BaseClass, Base):
    count = 0

    """Defines an option class"""
    __tablename__ = "options"
    serial: Mapped[int] = mapped_column(
        Integer, nullable=False, autoincrement=True)
    question_id: Mapped[str] = mapped_column(
        ForeignKey("questions.id", ondelete="CASCADE",
                   onupdate="CASCADE"), nullable=False)
    value: Mapped[str] = mapped_column(TEXT, nullable=False)
    votes: Mapped[str] = mapped_column(Integer, nullable=False, default=0)

    # relationship
    question: Mapped["Question"] = relationship(
        back_populates="options", single_parent=True)

    def __init__(self, *args, **kwargs):
        """Initializes an option instance"""
        if all([kwargs.get('question_id'), kwargs.get("value")]):
            super().__init__(*args, **kwargs)
