from sqlalchemy import Column, Integer
from sqlalchemy_utc import UtcDateTime, utcnow


class MixinWithID:
    id = Column(Integer(), primary_key=True, autoincrement=True)

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.id}>"


class MixinWithAutoNow:
    updated_at = Column(UtcDateTime(), nullable=False, default=utcnow(), onupdate=utcnow())
    created_at = Column(UtcDateTime(), nullable=False, default=utcnow())
