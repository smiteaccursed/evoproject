# Library service
Позволяет работать с книгами
# Если без докера
### Установка
- Установка зависимостей: `pip install -r requirements.txt `
- Подготовка .env файла: `PG_DSN = "postgresql://LOGIN:PASSWORD@IP:PORT/DBNAME"`

### Запуск с использование файла конфигурации .env

Для запуска из файла конфигурации нужно поместить файл .env в корень сервиса

### Конфигурация
| Переменная    | Назначение                      | Значение по-умолчанию                        |
| -----------   | -----                           | ---                                          |
| POSTGRES_DSN  | Строка подключения к PostgreSQL | postgresql://user:pass@localhost:5432/foobar |

### Значения POSTGRES_DSN для .env 
| Поле | Назначение |
|----- |-------|
| user | логин |
| pass | пароль|
| localhost | IP |
| 5432 | Порт |
| footbar | название БД |
## Запуск
uvicorn app.app:app --port 5000 --reload
# Если через docker
## Building 
`docker build -t "library" .`
## Запуск
Для запуска перейдите в папку `deploy` и проследуйте инструкциям
## Документация
Documentation: `http://localhost:5000/docs`


## Api
| Method | Route           | Description        |
|--------|-----------------|--------------------|
| POST   | `/books/`       | Add new book       |
| GET    | `/books/{bookID}` | Get book by ID    |
| DELETE | `/books/{bookID}` | Delete book by ID |
| PUT    | `/books/{bookID}` | Update book_info by ID |
| GET    | `/books/{userID}` | Get user book by ID    |
| DELETE |  `/books/{userID}`| Delete user book by ID |
