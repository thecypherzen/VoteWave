#!/usr/bin/python3
"""defines the base classes for models and database"""

from sqlalchemy import DateTime, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from uuid import uuid4
from datetime import datetime

format = "%Y-%m-%dT%H:%M:%S.%f"

def Base(DeclarativeBase):
    pass


class BaseClass():
    """The base clase for all models"""
    id: Mapped[str] = mapped_column(String(32), primary_key=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow())
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow())
    status: Mapped[str] = mapped_column(String(10), nullable=False, default="inactive")


    def __init__(self, *args, **kwargs):
        # handle empty kwargs
        if not kwargs:
            self.id = str(uuid4()).replace("-", "")
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at
        else:
            # set created_at
            if temp := kwargs.get("created_at") is None:
                self.created_at = datetime.utcnow()
            else:
                if isinstance(temp, str):
                    self.created_at = datetime.strptime(temp, format)
                elif isinstance(temp, datetime):
                    self.created_at = kwargs["created_at"]
                else:
                    self.created_at = datetime.utcnow()
                del kwargs["created_at"]
            # set updated_at
            if temp := kwargs.get("updated_at") is None:
                self.updated_at = self.created_at
            else:
                if isinstance(temp, str):
                    self.updated_at = datetime.strptime(temp, format)
                elif isinstance(temp, datetime):
                    self.updated_at = kwargs["updated_at"]
                else:
                    self.updated_at = datetime.utcnow()
                del kwargs["updated_at"]

    def __str__(self):
        """ Defines a string representation of class"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

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
