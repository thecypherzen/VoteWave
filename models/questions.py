 #!/usr/bin/python3
"""defines the user class"""


from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.base_class import BaseClass


class Question(BaseClass):
    __count = 0

    """Defines a user class"""
    __tablename__ = "questions"
    serial: Mapped[int] = mapped_column(Integer, nullable=False,
                                        autoincrement=True)
    poll_id: Mapped[str] = mapped_column(String(32), nullable=False)
    title: Mapped[str] = mapped_column(String(128), nullable=False)
    runner_text: Mapped[str] = mapped_column(String(128), nullable=False)
    location: Mapped[str] = mapped_column(String(255), nullable=False)
    """
    options = relationship()
    metadata = relationship()
    """

    def __init__(self, *args, **kwargs):
        """Initialize user class"""
        to_delete = ["poll_id", "location", "serial", "title", "runner_text"]
        if kwargs:
            self.serial = Question.__count + 1
            self.poll_id = kwargs.get("poll_id")
            self.title = kwargs.get("poll_id")
            self.runner_text = kwargs.get("runner_text")
            self.location = "/votewave/user/polls/poll_id/questions/question_id"
            for item in to_delete:
                if kwargs.get(item):
                    del kwargs[item]
            super().__init__(*args, **kwargs)
            Question.__count += 1
