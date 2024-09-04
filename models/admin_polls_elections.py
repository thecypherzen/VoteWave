#!/usr/bin/python3

from sqlalchemy import Column, ForeignKey, Integer, \
    String, Table, UniqueConstraint
from models.base_class import Base


# define admin_polls_elections relationship
admin_polls_elections = Table(
    "admin_polls_elections",
    Base.metadata,
    Column("id", Integer, autoincrement=True, primary_key=True),
    Column("admin_id", String(32),
           ForeignKey("admins.id", ondelete="CASCADE",
                      onupdate="CASCADE")),
    Column("poll_id", String(32),
           ForeignKey("polls.id", ondelete="CASCADE",
                      onupdate="CASCADE"), nullable=True),
    Column("election_id", String(32),
           ForeignKey("elections.id", ondelete="CASCADE",
                      onupdate="CASCADE"), nullable=True),
    UniqueConstraint("id", "admin_id", "poll_id", "election_id",
                     name="unique_admins")
)
