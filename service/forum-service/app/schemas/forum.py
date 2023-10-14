from pydantic import BaseModel, Field
from datetime import datetime
from typing import List
from uuid import UUID

class TopicBase(BaseModel):
    '''
    База ветки форума
    '''
    creator_id:UUID= Field(title='ID пользователя, создавшего ветку')
    name:str=Field(title="название ветки")


class TopicCreate(BaseModel):
    '''
    Модель создания ветки
    '''
    creator_id:UUID= Field(title='ID пользователя, создавшего ветку')
    name:str=Field(title="название ветки")


class TopicUpdate(TopicBase):
    '''
    Модель обновления ветки
    '''
    pass
class TopicMessageBase(BaseModel):
    
    text: str=Field(title="Текст сообщения")

class TopicMessage(TopicMessageBase):
    id:int=Field(title="ID сообщения")
    date:datetime=Field(title="Дата отправки")
    user_id:UUID= Field(title='ID пользователя')
    class Config:
        from_attributes = True


class Topic(TopicBase):
    '''
    модель ветки
    '''
    id:int=Field(title="ID ветки")
    messages:List[TopicMessage]=Field(title="Список сообщений", default=[])


class TopicMessageCreate(TopicMessageBase):
    user_id:UUID= Field(title='ID пользователя')
    class Config:
        from_attributes = True

class TopicMessageUpdate(TopicMessageBase):
    pass
