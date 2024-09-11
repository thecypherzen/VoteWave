#!/usr/bin/python3

from sqlalchemy import DateTime, ForeignKey, Integer, String, \
    UniqueConstraint
from sqlalchemy.ext.associationproxy import AssociationProxy, \
    association_proxy
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.base_class import Base, BaseClass
from typing import List


class UserWaitlist(BaseClass, Base):
    """Associates users with a waitlist"""
    count = 0
    __tablename__ = "users_waitlists"
    serial: Mapped[int] = mapped_column(
        Integer, nullable=False, autoincrement=True)
    user_id: Mapped[str] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE",
                   onupdate="CASCADE"))
    waitlist_id: Mapped[str] = mapped_column(
        ForeignKey("waitlists.id", ondelete="CASCADE",
                   onupdate="CASCADE"))
    join_as: Mapped[str] = mapped_column(
        String(16), nullable=False)
    UniqueConstraint("user_id", "waitlist_id")

    # relationships
    user: Mapped["User"] = relationship(
        back_populates="users_waitlists")
    waitlist: Mapped["Waitlist"] = relationship(
        back_populates="waitlist_users")


class Waitlist(BaseClass, Base):
    """Defines a waitlist class"""
    count = 0
    __tablename__ = "waitlists"
    serial: Mapped[int] = mapped_column(
        Integer, nullable=False, autoincrement=True)
    owner_id: Mapped[str] = mapped_column(
        ForeignKey("activities.id", ondelete="CASCADE",
                   onupdate="CASCADE"), unique=True)

    # relationships
    activity: Mapped["Activity"] = relationship(
        back_populates="waitlist")
    waitlist_users: Mapped[List["UserWaitlist"]] = relationship(
        back_populates="waitlist", cascade="all, delete-orphan")

    # association proxies
    users: AssociationProxy[List["UserWaitlist"]] = association_proxy(
        "waitlist_users", "user")


    def __init__(self, *args, **kwargs):
        """Initialises a the candidate class"""
        if kwargs and kwargs.get("owner_id"):
            super().__init__(*args, **kwargs)


    def add_user(self, user, join_as):
        """Adds many or one user to a waitlist"""
        res = {}
        try:
            user_waitlist = UserWaitlist(
                user=user, waitlist=self, join_as=join_as)
            user_waitlist.save()
            self.save()
            temp = {"success": True}
        except Exception as e:
            temp = {"success": False, "error": e}
        finally:
            res[f"{user.serial}"] = temp
        return res

    def remove_user(self, *users):
        """Removes many or one user from a waitlist"""
        res = {}
        for user in users:
            if isinstance(user, list):
                for usr in user:
                    if usr in self.users:
                        try:
                            self.users.remove(usr)
                            temp = {"success": True}
                        except Exception as e:
                            temp = {"success": False, "error": e}
                        finally:
                            res[f"{user.serial}"] = temp
            else:
                if user in self.users:
                    try:
                        self.users.remove(user)
                        temp = {"success": True}
                    except Exception as e:
                        temp = {"success": False, "error": e}
                    finally:
                        res[f"{user.serial}"] = temp
        self.save()
        return res


