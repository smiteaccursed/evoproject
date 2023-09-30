# library service
## Установка
- Настроить PostgreSQL в папке deploy. 
	- docker-compose up -d
- Подготовить виртуальное окружение
	- Добавить: `python3 -m venv venv`
	- Активировать: `venv/bin/activate`
	- Установить зависимости: `pip install -r requirements.txt` 

## Запуск
uvicorn app.app:app --port 5000 --reload

## Api
| Method | Route           | Description        |
|--------|-----------------|--------------------|
| GET    | `/books/`       | Get all books     |
| POST   | `/books/`       | Add new book       |
| GET    | `/books/{bookID}` | Get book by ID    |
| DELETE | `/books/{bookID}` | Delete book by ID |
| PUT    | `/books/{bookID}` | Update book_info by ID |
  
