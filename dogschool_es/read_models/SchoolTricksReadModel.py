from sqlalchemy.orm import DeclarativeBase
from datetime import datetime

from sqlalchemy import BigInteger, Column, DateTime, String, List, ARRAY

class Base(DeclarativeBase):
    pass


class TricksWithDogs(Base):
    __tablename__ = "tricks_with_dogs"

    trick_id = Column(String(255), primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    dogs = Column(String(255), nullable=False)
    date_added = Column(DateTime(timezone=True), default=datetime.utcnow)
    date_modified = Column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow)