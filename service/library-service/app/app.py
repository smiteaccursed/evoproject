from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse

from .schemas.library import Book, BookBase

from sqlalchemy.sql import text
from sqlalchemy.orm import Session

from .database import SessionLocal, engine, Base
import typing
from .schemas import Book, BookBase, BookUpdate
from . import crud

##______________##
## Инициализация
##______________##

Base.metadata.create_all(bind=engine)

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

## удаление

@app.delete("/books/{bookID}", 
            summary='Удаляет книгу из базы')

async def delete_book(bookID: int, db:Session=Depends(get_db)) -> Book :
    if crud.delete_book(db, bookID):
        return JSONResponse(status_code=200, content={"message": "Book deleted"})
    return JSONResponse(status_code=404, content={"message": "Book not found"})

## Обновление информации о книге 

@app.put("/books/{bookID}", 
         summary='Обновляет информацию о книге')

async def update_book(bookID: int, bookbase: BookUpdate, db:Session=Depends(get_db)) -> Book :
    book = crud.update_book(db, bookID, bookbase)
    if book!=None:
        return JSONResponse(status_code=200, content={"message": "Book successfully changed"})
    return JSONResponse(status_code=404, content={"message": "Item not found"})