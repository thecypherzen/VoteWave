#!/usr/bin/python3
"""defines the question class"""


from sqlalchemy import Boolean, ForeignKey, Integer, String
from sqlalchemy.dialects.mysql import TEXT
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.base_class import Base, BaseClass
from typing import List


class Question(BaseClass, Base):
    count = 0

    """Defines a question class"""
    __tablename__ = "questions"
    serial: Mapped[int] = mapped_column(
        Integer, nullable=False, autoincrement=True)
    poll_id: Mapped[str] = mapped_column(
        ForeignKey("polls.id", ondelete="CASCADE",
        onupdate="CASCADE"), nullable=False)
    title: Mapped[str] = mapped_column(TEXT, nullable=False)
    runner_text: Mapped[str] = mapped_column(String(128))
    multichoice: Mapped[bool] = mapped_column(
        Boolean, nullable=False, default=True)
    location: Mapped[str] = mapped_column(String(255), nullable=False)

    # relationships
    meta_data: Mapped[List["Metadata"]] = relationship(
        primaryjoin="and_(Question.id == Metadata.owner_id, \
        Metadata.owner_type =='question')",
        foreign_keys="Metadata.owner_id",
        cascade="all, delete-orphan",
        overlaps="_metadata,_metadata, _metadata, candidate, \
        election, meta_data, poll, user")
    """
    options = relationship()
    """

    def __init__(self, *args, **kwargs):
        """Initialize user class"""
        if all([kwargs.get("poll_id"), kwargs.get("title")]):
            items = ["location", "runner_text"]
            self.runner_text = kwargs.get("runner_text") or ""
            self.location = "location/for/question"
            for item in items:
                if kwargs.get(item):
                    del kwargs[item]
            super().__init__(*args, **kwargs)
