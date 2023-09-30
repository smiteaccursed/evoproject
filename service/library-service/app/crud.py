import typing

from sqlalchemy.orm import Session

from .database import models
from . import schemas

def create_book(
        db: Session, book: schemas.BookUpdate
    ) -> models.Book:
    '''
    Создает новую книгу в БД
    '''
    db_book = models.Book(
        book_id=book.id,
        name = book.name,
        rating = book.rating,
        genres = book.genres,
        type= book.type,
        authors = book.authors,
        series= book.series,
        about = book.about,
    )

    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_books(
        db: Session, skip: int = 0, limit: int = 100
    ) -> typing.List[models.Book]:
    '''
    Возвращает инфомрмацию о книгах
    '''
    return  db.query(models.Book) \
            .offset(skip) \
            .limit(limit) \
            .all()

def get_book_ID(
        db: Session, id: int
    ) -> models.Book:
    '''
    Возвращает информацию о конкретной книге
    '''
    return  db.query(models.Book) \
            .filter(models.Book.id == id) \
            .first()

def update_book(
        db: Session, book_id: int, book: schemas.BookUpdate
    ) -> models.Book:
    '''
    Обновляет информацию о книге
    '''
    
    result =    db.query(models.Book) \
                .filter(models.Book.id == book_id) \
                .update(book.dict())
    db.commit()

    if result == 1:
        return get_books(db, book_id)
    return None


def delete_book(
        db: Session, book_id: int
    ) -> bool:
    '''
    Удаляет информацию о книге 
    '''
    result =    db.query(models.Book) \
                .filter(models.Book.id == book_id) \
                .delete()
    db.commit()
    return result == 1