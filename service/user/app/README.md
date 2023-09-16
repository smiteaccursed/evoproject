# User service
## Running
uvicorn app.app:app --port 5020 --reload

## Api
| Method | Route           | Description        |
|--------|-----------------|--------------------|
| GET    | `/users/`       | Get all users      |
| POST   | `/users/`       | Add new user       |
| GET    | `/users/{userID}` | Get user by ID    |
| DELETE | `/users/{userID}` | Delete user by ID |
| PUT    | `/users/{userID}` | Update userinfo by ID |
  
