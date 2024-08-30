#!/urs/bin/python3
"""defines the base activity from which polls and
    elections will inherit
"""

from sqlalchemy import Boolean, DateTime, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import TEXT
from datetime import date, datetime
from models.base_class import BaseClass


format = "%Y-%m-%dT%H:%M:%S.%f"

class BaseActivity(BaseClass):
    """Defines a user class"""
    starts_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    ends_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    status: Mapped[str] = mapped_column(String(10), nullable=False)
    salt: Mapped[str] = mapped_column(String(16), nullable=False)
    security_key: Mapped[str] = mapped_column(String(128), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=False, default="")
    guidelines: Mapped[str] = mapped_column(TEXT, nullable=False, default="")
    is_public: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    owner_id: Mapped[str] = mapped_column(String(32), nullable=False)
    chatroom_id: Mapped[str] = mapped_column(String(32), nullable=False)
    retults: Mapped[str] = mapped_column(String(255), default="")

    def __init__(self, *args, **kwargs):
        """Initialize user class"""
        to_delete = ["starts_at", "ends_at", "salt", "description", "guidelines",
                     "is_public", "owner_id", "chatroom_id", "results", "security_key",
                     "status"]
        if kwargs:
            if (stime := kwargs.get("starts_at")).__class__.__name__ == "str":
                self.starts_at = datetime.strptime(stime, format)
            elif stime == "datetime":
                self.starts_at = stime
            if (etime := kwargs.get("ends_at ")).__class__.__name__ == "str":
                self.ends_at = datetime.strptime(etime, format)
            elif etime == "datetime":
                self.ends_at = etime
            self.status = kwargs.get("status") or "pending"
            self.salt = BaseActivity.generate_salt()
            self.security_key = BaseActivity.generate_hash(text=kwargs.get("security_key"),
                                                           salt=self.salt)
            self.description = kwargs.get("description") or ""
            self.guidelines = kwargs.get("guidelines") or ""
            self.is_public = kwargs.get("is_public") or True
            self.owner_id = kwargs.get("owner_id")
            self.chatroom_id = kwargs.get("chatroom_id") or \
                BaseActivity.new_chatroom() #.id
            self.results = kwargs.get("results") or ""
            for key in to_delete:
                if kwargs.get(key):
                    del kwargs[key]
        super().__init__(*args, **kwargs)


    @classmethod
    def new_chatroom(cls):
        """Creates a new chatroom instance
        Returns: id of new chatroom
        """
        return "983refpk"

    @property
    def admins(self):
        """Returns the list of admins of child activity"""
        pass

    @property
    def blacklist(self):
        """A getter that returns a list users blacklisted from child activty"""
        pass

    @property
    def chatroom(self):
        """returns the chatroom object"""
        pass

    @property
    def redflags(self):
        """A getter that returns a list users blacklisted from child activty"""
        pass

    @property
    def reviews(self):
        """A getter that returns a list of reviews for child activty"""
        pass

    @property
    def voters(self):
        """A getter that returns a list of voters in a child activty"""
        pass

    @property
    def waitlist(self):
        """A getter that returns a list of users on the waitlist of a child activty"""
        pass


    def create_invite(self):
        """Generates an invitation link for a newly created activity or its children"""
        pass

    def duration(self):
        """Claculates and returns the duration which an activity lasted
        """
        pass

    def generate_report(self):
         """Creates reports of an activity based on activity's results

            Return: dictionary of report
         """
         pass

    def share_with(self, link, users=[]):
        """sends an invitation link of the current event with another user
        Return: True on success, False on error
        """
        pass

    def update_blacklist(self, *blacklist_ids, add=True):
        """Updates an activity's blacklist.

        If add is True, items with the passed blacklist_ids are added,
            else, they are removed

        Returns: True on success or False on failure of any or all
        """
        pass

    def update_flags(self, *flag_ids, resolved=True):
        """Updates an activity's red flags, by updating their treated
        status to either True or false, based on the value of treated.

        Returns: True on success or False on failure of any or all
        """
        pass

    def update_reviews(self, *review_ids, add=True):
        """Updates an activity's list of reviews.

        If add is True, reviews with ppthe passed ids are added,
            else, they are removed

        Returns: True on success or False on failure of any or all
        """
        pass

    def update_voters(self, *voter_ids, add=True):
        """Updates an activity's list of voters.

        If add is True, voters with the passed user_ids are added,
            else, they are removed

        Returns: True on success or False on failure of any or all
        """
        pass

    def update_waitlist(self, *wait_ids, add=True):
        """Updates an activity's wait list.

        If add is True, wait list items with the passed ids are added,
            else, they are removed

        Returns: True on success or False on failure of any or all
        """
        pass
