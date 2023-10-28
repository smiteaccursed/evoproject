import typing, logging

from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session
from uuid import UUID

from .database.db import DB_INITIALIZER

from .schemas import Book
from .schemas import BookBase, BookUpdate
from . import crud, config
from typing import Optional

##______________##
## Инициализация
##______________##

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


# Создать все начальные данные
logger.info('Database initialization...')
SessionLocal = DB_INITIALIZER.init_db(cfg.pg_dsn.unicode_string())

#Получить доступ к базе данных
def get_db() -> Session:
    db = SessionLocal()
    try: yield db
    finally: db.close()

app = FastAPI(
    version='0.0.1',
    title='Library service'
)

## Список книг
tag_name="library"
@app.get("/books/UID/{userID}", 
        summary='Возвращает список книг', 
        response_model=list[Book],tags=[tag_name])
async def get_user_books(id: Optional[UUID]=None, db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> typing.Iterable[Book] :
    if id is not None:
        return crud.get_user_books(id, db, skip, limit)
    else:
        return crud.get_books(db, skip, limit)


## Создание новой книги

@app.post("/books", 
          response_model=Book,
          summary='Добавляет книгу в базу',tags=[tag_name])

async def add_book(book: BookBase, db:Session=Depends(get_db)) -> Book :
    return crud.create_book(db, book)

## книга по ID

@app.get("/books/BID/{bookID}", 
         summary='Возвращает информацию о книге',tags=[tag_name])

async def get_book_info(bookID: int, db: Session=Depends(get_db)) -> Book :
    book = crud.get_book_ID(db, bookID)
    if book ==None:
        return JSONResponse(status_code=404, content={"message": "Book not found..."})
    else:
        return book
    

## удаление

@app.delete("/books/BID/{bookID}", 
            summary='Удаляет книгу из базы',tags=[tag_name])

async def delete_book(bookID: int, db:Session=Depends(get_db)) -> Book :
    if crud.delete_book(db, bookID):
        return JSONResponse(status_code=200, content={"message": "Book deleted"})
    return JSONResponse(status_code=404, content={"message": "Book not found"})



## Удаление книг 

@app.delete("/books/UID/{userID}", 
            summary='Удаляет книги пользователя',tags=[tag_name])

async def delete_user_books(id: Optional[UUID] = None, db:Session=Depends(get_db)) -> Book :
    if id is not None:
        if crud.delete_user_books(db, id):
            return JSONResponse(status_code=200, content={"message": "Books deleted"})
    else:
         if crud.delete_all_books(db):
            return JSONResponse(status_code=200, content={"message": "All books deleted"})
    return JSONResponse(status_code=404, content={"message": "Error"})



## Обновление информации о книге 

@app.put("/books/{bookID}", 
         summary='Обновляет информацию о книге',tags=[tag_name])

async def update_book(bookID: int, bookbase: BookUpdate, db:Session=Depends(get_db)) -> Book :
    book = crud.update_book(db, bookID, bookbase)
    if book!=None:
        return JSONResponse(status_code=200, content={"message": "Book successfully changed"})
    return JSONResponse(status_code=404, content={"message": "Item not found"})
