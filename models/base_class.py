#!/usr/bin/python3
"""defines the base classes for models and database"""

from sqlalchemy import Datetime, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from uuid import uuid4
from datetime import datetime

format = "%Y-%m-%dT%H:%M:%S.%f"

def BaseClass():
    """The base clase for all models"""
    id: Mapped[str] = mapped_column(String(32), primary_key=True)
    created_at: Mapped[datetime] = maped_column(Datetime, default=datetime.utcnow())
    updated_at: Mapped[datetime] = mapped_column(Datetime, default=datetime.utcnow())
    status: Mapped[str] = mapped_column(String(10), nullable=False, default="inactive")


    def all(self):
        pass
    def create(self, **args):
        pass
    def destroy(self):
        pass
    def save(self):
        pass
    def to_dict(self):
        pass
    def update(self, *args):
        pass
