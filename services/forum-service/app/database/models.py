from sqlalchemy import Column, ForeignKey, Integer, String, JSON, Date, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
from .db import Base



class Topic(Base):
    __table_args__ = {'schema':  "forum"}
    __tablename__ = "Topic"
    id = Column(Integer, primary_key=True, index=True)
    creator_id = Column(UUID(as_uuid=True))
    name = Column(String)
    
    messages = relationship("TopicMessages", back_populates="topic")

class TopicMessages(Base):
    __tablename__ = "TopicMessages"
    __table_args__ = {'schema': "forum"}
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(UUID(as_uuid=True))
    text = Column(String)
    date = Column(Date)
    topic_id = Column(Integer, ForeignKey("forum.Topic.id"))
    topic = relationship("Topic", back_populates="messages")

    