import unittest

from app import schemas
from sqlalchemy.orm import Session
from app import crud
from fastapi import Depends

from app.database.db import DB_INITIALIZER

pg_dsn = 'postgresql://book:book@127.0.0.1:5432/library'

SessionLocal = DB_INITIALIZER.init_db(pg_dsn)

# Получить доступ к базе данных
def get_db() -> Session:
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()

class LibraryTestClass(unittest.TestCase):
    def setUp(self):
        self.db = get_db()
        self.book_data = schemas.BookUpdate(
            name='Test Book',
            user_id='3fa85f64-5717-4562-b3fc-2c963f66afa6',
            rating=8,
            genres=['Fiction'],
            type='Fiction',
            status=1,
            authors=['Author1'],
            series='Series1',
            about='A great test book'
        )

    def test_create_book(self):
        created_book = crud.create_book(self.db, self.book_data)
        bid=created_book.id
        self.assertIsNotNone(created_book.id)
        self.assertEqual(created_book.name, self.book_data.name)
        crud.delete_book(self.db, bid)
    def test_get_book(self):
        created_book = crud.create_book(self.db, self.book_data)
        self.assertIsNotNone(created_book.id)
        self.assertEqual(created_book.name, self.book_data.name)
        bid=created_book.id
        getted_book=crud.get_book_ID(self.db, bid)
        self.assertEqual(getted_book.name, self.book_data.name)
        crud.delete_book(self.db, bid)
        self.assertIsNone(crud.get_book_ID(self.db, bid))
    def test_update_book(self):
        created_book = crud.create_book(self.db, self.book_data)
        bid=created_book.id
        new_data=self.book_data
        new_data.name="change book"
        crud.update_book(self.db,bid, new_data)
        updated_book=crud.get_book_ID(self.db, bid)
        self.assertEqual(updated_book.name, new_data.name)
        crud.delete_book(self.db, bid)
        self.assertIsNone(crud.get_book_ID(self.db, bid))


