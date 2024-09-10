#!/usr/bin/python3

from models.base_class import Base, BaseClass
from models.base_activity import Activity
from models.admins import Admin
from models.blacklist import Blacklist
from models.candidates import Candidate
from models.chatrooms import Chatroom
from models.elections import Election
from models.inboxes import Inbox
from models.invitations import Invitation
from models.messages import Message
from models.messages import MessageInbox
from models.messages import MessageMetadata
from models.metadata import Metadata
from models.notices import Notice
from models.options import Option
from models.polls import Poll
from models.questions import Question
from models.redflags import Redflag
from models.reviews import Review
from models.users import User
from models.voters import Voter
from models.waitlists import Waitlist
from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv


class Storage():
    """Defines the apps' storage manager"""
    __session = None
    __mode = getenv("VW_ENV")
    __models = {"Admin":Admin, "Blacklist":Blacklist, "Candidate":Candidate,
                "Chatroom":Chatroom, "Election":Election, "Inbox": Inbox,
                "Invitation":Invitation, "Message": Message, "Metadata":Metadata,
                "Notice":Notice, "Option":Option, "Poll":Poll,
                "Question":Question, "Redflag":Redflag, "Review":Review,
                "User":User, "Voter":Voter, "Waitlist":Waitlist}

    if __mode == "test":
        DB_NAME = getenv("VW_TEST_DB")
        DB_USER = getenv("VW_TEST_USER")
        DB_PWD = getenv("VW_TEST_PWD")
        DB_HOST = getenv("VW_TEST_HOST")
    else:
        DB_NAME = getenv("VW_LIVE_DB")
        DB_USER = getenv("VW_LIVE_USER")
        DB_PWD = getenv("VW_LIVE_PWD")
        DB_HOST = getenv("VW_LIVE_HOST")

    uri = f"mysql+mysqldb://{DB_USER}:{DB_PWD}@{DB_HOST}/{DB_NAME}"
    __engine = create_engine(uri, pool_pre_ping=True)

    def __init__(self):
        self.__session = scoped_session(sessionmaker(bind=self.__engine))
        Base.metadata.create_all(self.__engine)


    def add(self, *objs):
        """adds a new object to storage session"""
        for obj in objs:
            if isinstance(obj, list):
                self.__session.add_all(obj)
            else:
                self.__session.add(obj)

    def all(self, obj=None):
        """gets all instanes of a class type from storag"""
        found_models = []
        if not obj:
            for model in self.__models.values():
                found_models += self.__session.query(model).all()
            return found_models
        elif not (toget := self.resolve_model(obj)):
            return found_models
        return self.__session.query(toget).all()


    def close(self):
        """closes the current session"""
        self.__session.close()


    def delete(self, obj):
        """Removes an object from storage"""
        self.__session.delete(obj)
        self.__session.commit()

    def get(self, toget, id):
        """Returns a particular"""
        if not (obj := self.resolve_model(toget)):
            return None
        all_items = self.all(obj)
        for item in all_items:
            if item.id == id:
                return item
        return None

    def get_last_of(self, clsname):
        """returns the last object of classname in storage if
        exists or None if not exists
        """
        if not (obj := self.resolve_model(clsname)):
            return None
        last_of = self.__session.query(obj).order_by(desc(obj.serial)).first()
        return last_of or None

    def resolve_model(self, toget):
        """resolves a model's name or object if it exists or None"""
        if isinstance(toget, str):
            if toget in self.__models:
                return self.__models[toget]
            return None
        else:
            if toget in self.__models.values():
                return toget
        return None

    def reload(self):
        """Reloads database connections"""
        self.__session.remove()


    def save(self):
        """Saves current session to storage"""
        self.__session.commit()





