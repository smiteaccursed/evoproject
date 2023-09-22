# library service
## Running
uvicorn app.app:app --port 5000 --reload

## Api
| Method | Route           | Description        |
|--------|-----------------|--------------------|
| GET    | `/books/`       | Get all books     |
| POST   | `/books/`       | Add new book       |
| GET    | `/books/{bookID}` | Get book by ID    |
| DELETE | `/books/{bookID}` | Delete book by ID |
| PUT    | `/books/{bookID}` | Update book_info by ID |
  
![image](https://github.com/smiteaccursed/evoproject/assets/144155604/caed390e-5234-4d3a-9e63-34a75246dfbb)
