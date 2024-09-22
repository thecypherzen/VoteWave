#!/usr/bin/python3
"""defines the base classes for models and database"""


from sqlalchemy import DateTime, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from uuid import uuid4
from datetime import datetime
import hashlib
import models
import secrets
import string

format = "%Y-%m-%dT%H:%M:%S.%f"



class Base(DeclarativeBase):
    pass


class BaseClass():
    """The base clase for all models"""
    id: Mapped[str] = mapped_column(
        String(32),primary_key=True, index=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow())
    status: Mapped[str] = mapped_column(
        String(10), nullable=False, default="inactive")
    deleted_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=True)

    def __init__(self, *args, **kwargs):
        # handle empty kwargs
        self.__class__.count += 1
        self.serial = self.get_serial(self, self.count)
        if not kwargs:
            self.id = str(uuid4()).replace("-", "")
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at
        else:
            # set created_at
            if not (temp := kwargs.get("created_at")):
                self.created_at = datetime.utcnow()
            else:
                if isinstance(temp, str):
                    self.created_at = datetime.strptime(temp, format)
                elif temp.__class__.__name__ == "datetime":
                    self.created_at = kwargs["created_at"]
                else:
                    self.created_at = datetime.utcnow()
                del kwargs["created_at"]

            # set updated_at
            if not (temp := kwargs.get("updated_at")):
                self.updated_at = self.created_at
            else:
                if isinstance(temp, str):
                    self.updated_at = datetime.strptime(temp, format)
                elif temp.__class__.__name__ == "datetime":
                    self.updated_at = kwargs["updated_at"]
                else:
                    self.updated_at = datetime.utcnow()
                del kwargs["updated_at"]

            # set id
            if not (temp := kwargs.get("id")):
                self.id = str(uuid4()).replace("-", "")
            else:
                if isinstance(temp, str) and len(temp) == 32:
                    self.id = temp
                else:
                    self.id = str(uuid4()).replace("-", "")
                del kwargs["id"]

            # create inbox
            if (name := self.__class__.__name__) == "User" or \
               name == "Election" or name == "Poll":
                self.create_inbox()

            if temp := kwargs.get("__class__"):
                del kwargs["__class__"]


            # set rest
            for key, value in kwargs.items():
                setattr(self, key, value)


    @classmethod
    def all(self) -> list:
        """ Returns all instances of current class"""
        return models.storage.all(self.__name__)

    @classmethod
    def all_deleted(self) -> list:
        """Returns all deleted instances of an object"""
        return models.storage.trashed(self.__name__)
    @classmethod
    def get(self, id):
        """Returns an a class instance with matched id or
        None if not found
        """
        return models.storage.get(self, id)

    @classmethod
    def generate_hash(cls, salt=None, text=None, chars=128):
        """Creates and returns a hash from a string"""
        if any([not text, not salt]):
            return None
        return hashlib.sha512(salt.encode("utf-8") +
                              text.encode("utf-8")).hexdigest()[:chars]

    @classmethod
    def generate_salt(cls, chars=16):
        """Creates a returns a random salt """
        return secrets.token_hex(chars//2)

    @classmethod
    def get_serial(cls, instance, count):
        """Gets the next serial for an instance"""
        cls_name = instance.__class__.__name__
        if not (last_obj := models.storage.get_last_of(cls_name)):
            return count
        return last_obj.serial + 1

    @classmethod
    def random_string(cls, chars=32):
        """generates a new hash from"""
        charset = string.ascii_letters + string.digits
        bytes = secrets.token_bytes(chars)
        return "".join(secrets.choice(charset) for _ in range(chars))


    @property
    def blacklist(self):
        """A getter that returns a list users blacklisted by
        an activty instance"""
        if (entries := self.blacklist_entries):
            from models import storage
            return [storage.get("User", entry.blocked_user_id)
                    for entry in entries]
        else:
            return None

    @property
    def is_deleted(self):
        """Returns True if instnace is deleted else False"""
        return self.deleted_at is not None

    @property
    def received_messages(self):
        """Returns an instances messages from their inbox"""
        if not hasattr(self, "inbox"):
            return None
        return self.inbox.messages if self.inbox else None

    @property
    def sent_messages(self):
        """Returns messages sent by a user"""
        from models import storage

        if any([(name := self.__class__.__name__) == "Voter",
                name == "Candidate", name == "Election",
                name == "Poll"]):
            return self.sent_messages
        return None


    def __str__(self):
        """ Defines a string representation of class"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}" \
            if self.id else "None"


    def create_inbox(self):
        """Creates and Returns a new inbox instance"""
        from models.inboxes import Inbox
        from models import storage

        owner_type = self.__class__.__name__.lower()
        if owner_type == "user" or owner_type == "election" or \
           owner_type == "poll":
            storage.add(Inbox(owner_id=self.id, owner_type=owner_type))
            storage.save()

    def destroy(self):
        """ Deletes current instance of object from storage"""
        models.storage.delete(self)
        return True

    def restore(self: object) -> object:
        """Restores deleted instance of object"""
        models.storage.restore(self)
        return True

    def save(self):
        """ Saves current instance of object to storage"""
        models.storage.add(self)
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary representation of current object instance"""
        to_remove = ["_sa_instance_state", "salt", "security_key",
                     "passwd_hash", "serial", "deleted_at"]
        dates = ["starts_at", "ends_at", "dob"]
        obj_copy = self.__dict__.copy()
        obj_copy["__class__"] = self.__class__.__name__
        obj_copy["created_at"] = self.created_at.isoformat()
        obj_copy["updated_at"] = self.updated_at.isoformat()
        for date in dates:
            if obj_copy.get(date):
                obj_copy[date] = obj_copy[date].isoformat()

        # remove internal values
        for item in to_remove:
            if item in obj_copy:
                del obj_copy[item]
        return obj_copy


    def update(self, **args):
        """Updates values of current instance with passed kwargs"""
        pass

    def update_metadata(self, value, delete=True):
        """updates an instance's metadata
           If `delete` is True, the instance with `value` is deleted, else
           If the instance's metadata is updted based on `value`, which is
            expected in the format:
            {"metadata_id": "value":"<new_value>"}}

        Returns: True on success or False on failure of any or all
            """
        pass

    def verify_pass_token(self, text, password=False):
        """Verify if token matches previous values"""
        if not self.salt:
            return False
        hash = self.generate_hash(salt=self.salt, text=text)
        if password:
            if not hasattr(self, "passwd_hash"):
                return False
            return hash == self.passwd_hash
        if not hasattr(self, "security_key"):
            return False
        return hash == self.security_key

