#!/urs/bin/python3
"""defines the base activity from which polls and
    elections will inherit
"""

from sqlalchemy import Boolean, DateTime, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.mysql import TEXT
from datetime import date, datetime
from models.base_class import BaseClass, Base


format = "%Y-%m-%dT%H:%M:%S.%f"


class Activity(BaseClass, Base):
    """Defines an Activity Class"""
    count = 0
    __tablename__ = "activities"
    starts_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    ends_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    status: Mapped[str] = mapped_column(String(10), nullable=False)
    salt: Mapped[str] = mapped_column(String(16), nullable=False)
    security_key: Mapped[str] = mapped_column(String(128),
                                              nullable=False)
    description: Mapped[str] = mapped_column(String(255),
                                             nullable=False, default="")
    guidelines: Mapped[str] = mapped_column(TEXT, nullable=False, default="")
    is_public: Mapped[bool] = mapped_column(Boolean, nullable=False,
                                            default=True)
    owner_id: Mapped[str] = mapped_column(ForeignKey("users.id"))
    results: Mapped[str] = mapped_column(String(255), default="")
    type: Mapped[str] = mapped_column(String(32))

    # relationships
    waitlist: Mapped["Waitlist"] = relationship(
        back_populates="activity")

    __mapper_args__ = {"polymorphic_abstract": True,
                     "polymorphic_on": "type"}


    def __init__(self, *args, **kwargs):
        """Initialize user class"""
        to_delete = ["starts_at", "ends_at", "salt", "description",
                     "guidelines", "is_public", "user_id", "chatroom_id",
                     "results", "security_key", "status"]
        if kwargs:
            if (stime := kwargs.get("starts_at")).__class__.__name__ == "str":
                self.starts_at = datetime.strptime(stime, format)
            elif stime.__class__.__name__ == "datetime":
                self.starts_at = stime
            if (etime := kwargs.get("ends_at")).__class__.__name__ == "str":
                self.ends_at = datetime.strptime(etime, format)
            elif etime.__class__.__name__ == "datetime":
                self.ends_at = etime
            self.status = "pending"
            self.salt = self.generate_salt()
            self.security_key = self.generate_hash(
                text=kwargs.get("security_key"), salt=self.salt)
            self.description = kwargs.get("description") or ""
            self.guidelines = kwargs.get("guidelines") or ""
            self.is_public = kwargs.get("is_public") or True
            self.owner_id = kwargs.get("user_id")
            self.results = kwargs.get("results") or ""
            for key in to_delete:
                if kwargs.get(key):
                    del kwargs[key]
        super().__init__(*args, **kwargs)

    def set_live_end(self):
        """Sets the status of an activity model
        to either live or ended depending on its
        start_at and ends_at values
        """
        starts_diff = self.starts_at - self.created_at
        ends_diff = self.ends_at - self.created_at
        now = datetime.now() - self.created_at

        print("STATUS BEFORE: ", self.status)
        if now >= starts_diff:
            if now < ends_diff:
                self.status = "live"
            elif now >= ends_diff:
                self.status = "ended"
        print("STATUS AFTER: ", self.status)
        #self.save()

