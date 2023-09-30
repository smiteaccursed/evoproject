# library service
## ���������
- ��������� PostgreSQL � ����� deploy. 
	- docker-compose up -d
- ����������� ����������� ���������
	- ��������: `python3 -m venv venv`
	- ������������: `venv/bin/activate`
	- ���������� �����������: `pip install -r requirements.txt` 

## ������
uvicorn app.app:app --port 5000 --reload

## Api
| Method | Route           | Description        |
|--------|-----------------|--------------------|
| GET    | `/books/`       | Get all books     |
| POST   | `/books/`       | Add new book       |
| GET    | `/books/{bookID}` | Get book by ID    |
| DELETE | `/books/{bookID}` | Delete book by ID |
| PUT    | `/books/{bookID}` | Update book_info by ID |
  
