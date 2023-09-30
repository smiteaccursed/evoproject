from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, JSON

from .db import Base

class Book(Base):
    __tablename__ = "library"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    rating=Column(Integer,info={'min': 0, 'max': 10})

    genres=Column(JSON)
    type=Column(String)
    authors=Column(JSON)
    series=Column(String)
    about=Column(JSON)