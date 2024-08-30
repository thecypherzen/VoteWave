#!/urs/bin/python3
"""defines the base activity from which polls and
    elections will inherit
"""

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date, datetime
from models.base_activity import BaseActivity


class Election(BaseActivity):
    """Defines a user class

    """
    __count = 0
    serial: Mapped[int] = mapped_column(Integer, nullable=False, autoincrement=True)
    location: Mapped[str] = mapped_column(String(255), nullable=False)
    title: Mapped[str] = mapped_column(String(128), nullable=False)
    """
    admins = relationship()
    candidates = relationship()
    voters = relationship()
    reviews = relationship()
    waitlist = relatiohship()
    redflags = relationship()
    metadata = relationship()
    notices = relationship()
    inbox = relationship()
    """

    def __init__(self, *args, **kwargs):
        """Initialize user class"""
        if all([kwargs.get("starts_at"), kwargs.get("ends_at"), kwargs.get("security_key")]):
            if (title := kwargs.get("title")):
                self.title = title
                del kwargs["title"]
            else:
                self.title = f"Election-{Election.__count + 1}"
            self.location = "votewave/user_id/elections/election_id"

            super().__init__(*args, **kwargs)


    @property
    def admins(self):
        """Returns the list of admins of child activity"""
        pass

    @property
    def blacklist(self):
        """A getter that returns a list users blacklisted from child activty"""
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

    def update_flags(self, *flag_ids, treated=True):
        """Updates an activity's red flags, by updating their treated
        status to either True or false, based on the value of treated.

        Returns: True on success or False on failure of any or all
        """
        pass

    def update_metadata(self, *meta_ids, add=True):
        """Updates an activity's list of metadata.

        If add is True, metadata with the passed ids are added,
            else, they are removed

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
