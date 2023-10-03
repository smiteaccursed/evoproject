import typing, logging

from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session

from .database.db import DB_INITIALIZER

from .schemas import Book
from .schemas import BookBase, BookUpdate
from . import crud, config

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

@app.get("/books", 
        summary='Возвращает список всех книг', 
        response_model=list[Book])
async def get_books_list(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> typing.Iterable[Book] :
    return crud.get_books(db, skip, limit)

## Создание новой книги

@app.post("/books", 
          response_model=Book,
          summary='Добавляет книгу в базу')

async def add_book(book: BookBase, db:Session=Depends(get_db)) -> Book :
    return crud.create_book(db, book)

## книга по ID

@app.get("/books/{bookID}", 
         summary='Возвращает информацию о книге')

async def get_book_info(bookID: int, db: Session=Depends(get_db)) -> Book :
    book = crud.get_book_ID(db, bookID)
    if book ==None:
        return JSONResponse(status_code=404, content={"message": "Book not found..."})
    else:
        return book
    
## Книги по userid

@app.get("/user_books/{userID}", 
        summary='Возвращает список книг пользоватея', 
        response_model=list[Book])
async def get_user_books(id:int, db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> typing.Iterable[Book] :
    return crud.get_user_books(id, db, skip, limit)

## удаление

@app.delete("/books/{bookID}", 
            summary='Удаляет книгу из базы')

async def delete_book(bookID: int, db:Session=Depends(get_db)) -> Book :
    if crud.delete_book(db, bookID):
        return JSONResponse(status_code=200, content={"message": "Book deleted"})
    return JSONResponse(status_code=404, content={"message": "Book not found"})

## Удаление ВСЕХ книг

@app.delete("/booksall/", 
            summary='Удаляет ВСЕ книги из базы')

async def delete_books(db:Session=Depends(get_db)) -> Book :
    if crud.delete_books(db):
        return JSONResponse(status_code=200, content={"message": "Books deleted"})
    return JSONResponse(status_code=404, content={"message": "Error"})

## Удаление ВСЕХ книг ПОЛЬЗОВАТЕЛЯ

@app.delete("/user_booksall/", 
            summary='Удаляет ВСЕ книги Пользователя')

async def delete_user_books(id: int, db:Session=Depends(get_db)) -> Book :
    if crud.delete_user_books(db, id):
        return JSONResponse(status_code=200, content={"message": "Books deleted"})
    return JSONResponse(status_code=404, content={"message": "Error"})



## Обновление информации о книге 

@app.put("/books/{bookID}", 
         summary='Обновляет информацию о книге')

async def update_book(bookID: int, bookbase: BookUpdate, db:Session=Depends(get_db)) -> Book :
    book = crud.update_book(db, bookID, bookbase)
    if book!=None:
        return JSONResponse(status_code=200, content={"message": "Book successfully changed"})
    return JSONResponse(status_code=404, content={"message": "Item not found"})