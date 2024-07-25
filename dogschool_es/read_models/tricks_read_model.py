from sqlalchemy.orm import DeclarativeBase
from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, String

class Base(DeclarativeBase):
    pass


class TricksWithDogs(Base):
    __tablename__ = "tricks_with_dogs"

    trick_id = Column(String(255), primary_key=True)
    name = Column(String(255), nullable=False, unique=False)
    dog_names = Column(String(255), nullable=False)
    date_added = Column(DateTime(timezone=True), default=datetime.now(timezone.utc))
    date_modified = Column(DateTime(timezone=True),  default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))