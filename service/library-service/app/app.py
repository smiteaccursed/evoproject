from fastapi import FastAPI
from fastapi.responses import JSONResponse

from .schemas.library import Book, BookBase

import typing

app = FastAPI(
    version='0.0.1',
    title='Library service'
)

books: typing.Dict[int, Book] = {}

@app.get("/books", summary='Возвращает список всех книг', response_model=list[Book])
async def get_books_list() -> typing.Iterable[Book] :
    return [ v for k,v in books.items() ]

@app.post("/books", status_code=201, response_model=Book,summary='Добавляет книгу в базу')
async def add_book(book: BookBase) -> Book :
    result = Book(
        **book.model_dump(),
        id=len(books) + 1
    )
    books[result.id] = result
    return result

@app.get("/books/{bookID}", summary='Возвращает информацию о книге')
async def get_book_info(bookID: int) -> Book :
    if bookID in books: return books[bookID]
    return JSONResponse(status_code=502, content={"message": "Not found!"})

@app.delete("/books/{bookID}", summary='Удаляет книгу из базы')
async def delete_book(bookID: int) -> Book :
    if bookID in books:
        del books[bookID]
        return JSONResponse(status_code=200, content={"message": "Deleted!"})
    return JSONResponse(status_code=404, content={"message": "Not found!"})

@app.put("/books/{bookID}", summary='Обновляет информацию о книге')
async def update_book(bookID: int, bookbase: BookBase) -> Book :
    if bookID in books:
        result = Book(
            **bookbase.model_dump(),
            id=bookID
        )
        books[bookID] = result
        return books[bookID]
    return JSONResponse(status_code=404, content={"message": "Item not found"})