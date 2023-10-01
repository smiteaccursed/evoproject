# library service
## Installation
- Configure PostgreSQL in the deploy folder. 
 	- docker-compose up -d
- Prepare a virtual environment
	 - Add: `python3 -m venv venv`
 	- Activate: `venv/bin/activate`
 	- Install dependencies: `pip install -r requirements.txt ` 

## Start
uvicorn app.app:app --port 5000 --reload

## Api
| Method | Route           | Description        |
|--------|-----------------|--------------------|
| GET    | `/books/`       | Get all books     |
| POST   | `/books/`       | Add new book       |
| GET    | `/books/{bookID}` | Get book by ID    |
| DELETE | `/books/{bookID}` | Delete book by ID |
| PUT    | `/books/{bookID}` | Update book_info by ID |
  
