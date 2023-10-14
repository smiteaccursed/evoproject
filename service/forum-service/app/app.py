import typing, logging

from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session
from uuid import UUID

from .database.db import DB_INITIALIZER

from .schemas import TopicMessage, TopicMessageBase, TopicMessageCreate, TopicMessageUpdate
from .schemas import TopicBase, TopicUpdate, TopicCreate, Topic
from . import crud, config


logger = logging.getLogger(__name__)
logging.basicConfig(
    level=20,
    format="%(levelname)-9s %(message)s"
)

logger.info("Configuration loading...")
cfg: config.Config = config.load_config(_env_file='.env')
logger.info(
    'Service configuration loaded:\n' +
    f'{cfg.model_dump_json(by_alias=True, indent=4)}'
)
logger.info('Database initialization...')
SessionLocal = DB_INITIALIZER.init_db(cfg.pg_dsn.unicode_string())

#Получить доступ к базе данных
def get_db() -> Session:
    db = SessionLocal()
    try: yield db
    finally: db.close()

app = FastAPI(
    version='0.0.1',
    title='Forum service'
)

## МЕТОДЫ ВЕТОК 
## все топики
@app.get("/topics", summary="Возвращает список всех веток",response_model=list[Topic])
async def get_topics(db:Session=Depends(get_db), skip: int = 0, limit: int = 100):
    return crud.get_topics(db, skip, limit)


##топик по id
@app.get("/topics/{topicID}", 
         summary='Получение топика по ID'
)
async def get_topic_info(topicID: int, db: Session = Depends(get_db)) -> Topic :
    topic = crud.get_topic_by_id(db, topicID)
    if topic != None:
        return topic
    return JSONResponse(status_code=404, content={"message": "Topic not found"})

##удаление топика 
@app.delete("/topics/{topicID}", 
            summary='Удаляет топик из базы по ID'
)
async def delete_topic(topicID: int, db: Session = Depends(get_db)) -> Topic :
    if crud.remove_topic_by_id(db, topicID):
        return JSONResponse(status_code=200, content={"message": "Topic successfully deleted"})
    return JSONResponse(status_code=404, content={"message": "Topic not found"})

##обновление топика
@app.put("/topics/{topicID}", 
         summary='Обновляет топика по ID'
)
async def update_topic(topicID: int, topicbase: TopicUpdate, db: Session = Depends(get_db)) -> Topic :
    topic = crud.update_topic(db, topicID, topicbase)
    if topic != None:
        return JSONResponse(status_code=200, content={"message": "Topic successfully changed"})
    return JSONResponse(status_code=404, content={"message": "Topic not found"})

## добавление топика
@app.post("/topics", response_model=Topic, summary='Добавляет ветку')
async def add_topic(topic:TopicBase, db:Session=Depends(get_db))->Topic:
    return crud.create_topic(db, topic)

##__________________##
## МЕТОДЫ СООБЩЕНИЙ ##

@app.post("/topics/{topicID}/message", summary='Отправка сообщения в топик')

async def send_message(topicID: int, topic_message:TopicMessageCreate, db: Session = Depends(get_db)) ->TopicMessage:
    topic=crud.get_topic_by_id(db, topicID)
    if topic!=None:
        mess=crud.send_message(db, topic,topic_message)
        if mess !=None:
            return mess
        return JSONResponse(status_code=500, content={"message": "Message not created"})
    return JSONResponse(status_code=404, content={"message": "Topic not found"})

## получение
@app.get("/messages/{messageID}", 
         summary='Получить сообщение по id',
         response_model=TopicMessage,
)
async def get_message_by_id(messageID: int, db: Session = Depends(get_db)) -> TopicMessage :
    message = crud.get_message(db, messageID)
    if message != None:
        return message
    return JSONResponse(status_code=404, content={"message": "Message not found"})
## обновление 
@app.put("/messages/{messageID}", 
         summary='Обновляет сообщение по его ID'
)
async def update_message(messageID: int, messagebase: TopicMessageBase, db: Session = Depends(get_db))  :
    status = crud.update_message(db, messageID, messagebase)
    if status != None:
        return JSONResponse(status_code=200, content={"message": "Message successfully changed"})
    return JSONResponse(status_code=404, content={"message": "Message not found"})



