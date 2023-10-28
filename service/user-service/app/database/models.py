from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase

from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import mapped_column, relationship

from app.database import db

class Group(db.BASE):
    __tablename__  = 'group'
    id = Column(Integer, primary_key=True , autoincrement=True, index=True)
    name = Column(String)

class User(SQLAlchemyBaseUserTableUUID, db.BASE):
    __table_args__ = {'schema':  db.SCHEMA}

    nickname = Column(String(length=128), nullable=True)
    bio = Column(String(length=1024), nullable=True)
    group_id = mapped_column(ForeignKey("group.id"))
    ban=Column(Boolean)
    group = relationship("Group", uselist=False)


async def get_user_db(session: AsyncSession = Depends(db.get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)