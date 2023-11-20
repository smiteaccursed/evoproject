import typing
from sqlalchemy.orm import Session
from sqlalchemy.dialects.postgresql import UUID

from .database import models
from . import schemas

def create_book(
        db: Session, book: schemas.BookUpdate
    ) -> models.Book:
    '''
    Создает новую книгу в БД
    '''
    db_book = models.Book(
        name = book.name,
        user_id=book.user_id,
        rating = book.rating,
        genres = book.genres,
        type= book.type,
        status = book.status,
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
    return db.query(models.Book) \
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


def get_user_books(
         id: UUID, db: Session, skip: int = 0, limit: int = 100
    ) -> models.Book:
    '''
    Возвращает информацию о книгах пользователя
    '''
    return  db.query(models.Book) \
            .filter(models.Book.user_id== id) \
            .offset(skip) \
            .limit(limit)\
            .all()

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

def delete_books(db: Session) -> bool:
    '''
    Удаляет ВСЕ книги
    '''
    result = db.query(models.Book).delete()
    db.commit()
    return result > 0

def delete_user_books(db: Session, id:UUID) -> bool:
     '''
    Удаляет ВСЕ книги ПОЛЬЗОВАТЕЛЯ
    '''
     result =    db.query(models.Book) \
                .filter(models.Book.user_id ==id) \
                .delete()
     db.commit()
     return result>0
