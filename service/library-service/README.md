# library service
## Установка
- Установка зависимостей: `pip install -r requirements.txt `
- Подготовка .env файла: `PG_DSN = "postgresql://LOGIN:PASSWORD@IP:PORT/DBNAME"`

## Запуск
uvicorn app.app:app --port 5000 --reload

## Документация
Documentation: `http://localhost:5000/docs`


## Api
| Method | Route           | Description        |
|--------|-----------------|--------------------|
| GET    | `/books/`       | Get all books     |
| POST   | `/books/`       | Add new book       |
| GET    | `/books/{bookID}` | Get book by ID    |
| DELETE | `/books/{bookID}` | Delete book by ID |
| PUT    | `/books/{bookID}` | Update book_info by ID |
| DELET |  | Delete all books |
| GET    | `/userbooks/{userID}` | Get user book by ID    |
| DELET |  `/userbooks/{userID}`| Delete user book by ID |
