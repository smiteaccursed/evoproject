from sqlalchemy import Column, Integer, String, JSON, Enum
from sqlalchemy.dialects.postgresql import UUID

from .db import Base
import enum
class BookStatus(enum.Enum):
    wanted=1
    available=2
    readed=3

class Book(Base):
    __tablename__ = "library"  
    __table_args__ = {'schema':  "library"}
    id = Column(Integer, primary_key=True, index=True, unique=True)
    user_id=Column(UUID(as_uuid=True))
    name = Column(String)
    status = Column(Enum(BookStatus), default=BookStatus.wanted)
    rating=Column(Integer,info={'min': 0, 'max': 10})

    genres=Column(JSON)
    type=Column(String)
    authors=Column(JSON)
    series=Column(String)
    about=Column(JSON)