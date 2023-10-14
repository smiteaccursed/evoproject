import typing

from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy.dialects.postgresql import UUID
from .database import models
from . import schemas

def create_topic_message(user_id:UUID, text: str):
    
    return models.TopicMessages(
        text=text,
        user_id=user_id,
        date=datetime.now(),
    )
def get_topics(db:Session, skip:int=0, limit:int=100)->typing.Iterable[models.Topic]:
    
    return db.query(models.Topic)\
        .offset(skip) \
        .limit(limit) \
        .all()

def create_topic(db:Session, topic: schemas.TopicCreate)->models.Topic:

    new_topic=models.Topic(
        creator_id=topic.creator_id,
        name=topic.name,
        
    )

    db.add(new_topic)
    db.commit()
    db.refresh(new_topic)
    return new_topic

def get_topic_by_id(db:Session, topic_id:int)-> models.Topic:

    return db.query(models.Topic)\
            .filter(models.Topic.id==topic_id) \
            .first()

def remove_topic_by_id(db: Session, topic_id:int) -> bool:

    topic = get_topic_by_id(db, topic_id)

    if topic != None:
        for message in topic.messages:
            db.delete(message)

        db.delete(topic)

        db.commit()
        return True
    return False

def update_topic(db:Session, topic_id: int, topic:schemas.TopicUpdate)->models.Topic:
    
    filter = db.query(models.Topic).filter(models.Topic.id == topic_id)
    result = filter.update(topic.model_dump())
    rtopic=filter.first()
    db.commit()
    if result == 1:
        return rtopic
    return None

def get_topic_messages(db:Session, topic: models.Topic)->typing.Iterable[models.TopicMessages]:
    return topic.messages

def send_message(db:Session, topic: models.Topic, topic_message: schemas.TopicMessageCreate):

    new_message = create_topic_message(topic_message.user_id,topic_message.text )
    topic.messages.append(new_message)
    db.commit()

    return new_message

def get_messages(db:Session, message_id:int):
    return db.query(models.TopicMessages) \
            .filter(models.TopicMessages.id == message_id) \
            .first()

def update_message(db:Session, message_id: int, message:schemas.TopicMessageUpdate) -> models.Topic:
    filter = db.query(models.TopicMessages).filter(models.TopicMessages.id==message_id)
    result = filter.update(message.model_dump())
    message = filter.first()
    db.commit()

    if result == 1:
        return message
    return None

