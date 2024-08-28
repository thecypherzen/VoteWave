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


    def all(self: object) -> list:
        """ Returns all instances of current class"""
        pass

    def create(self, **args):
        """ Creates instance of current class using passed kwargs"""
        pass

    def destroy(self):
        """ Deletes current instance of object from storage"""
        pass

    def save(self):
        """ Saves current instance of object to storage"""
        pass

    def to_dict(self):
        """Returns a dictionary representation of current object instance"""
        pass

    def update(self, **args):
        """Updates values of current instance with passed kwargs"""
        pass
