import datetime

from sqlalchemy import Column, Integer
from sqlalchemy_utc import UtcDateTime


class MixinWithID:
    id = Column(Integer(), primary_key=True, autoincrement=True)

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.id}>"


class MixinWithAutoNow:
    updated_at = Column(
        UtcDateTime(),
        nullable=False,
        default=lambda: datetime.datetime.utcnow(),
        onupdate=lambda: datetime.datetime.utcnow(),
    )
    created_at = Column(UtcDateTime(), nullable=False, default=lambda: datetime.datetime.utcnow())
