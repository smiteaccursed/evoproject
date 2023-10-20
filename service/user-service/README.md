# User service
# Если без докера
### Установка
- Установка зависимостей: `pip install -r requirements.txt `
- Подготовка .env файла:
- `PG_DSN = "postgresql://LOGIN:PASSWORD@IP:PORT/DBNAME"`
- `JWT_SECRET=JWT_SECRET`
- `RESET_PASSWORD_TOKEN_SECRET=RESET_PASSWORD_TOKEN_SECRET`
- `VERIFICATION_TOKEN_SECRET=VERIFICATION_TOKEN_SECRET `

### Запуск с использование файла конфигурации .env

Для запуска из файла конфигурации нужно поместить файл .env в корень сервиса

### Конфигурация
| Переменная    | Назначение                      | Значение по-умолчанию                        |
| -----------   | -----                           | ---                                          |
| POSTGRES_DSN  | Строка подключения к PostgreSQL | postgresql://user:pass@localhost:5432/foobar |
|JWT_SECRET ||JWT_SECRET|
|RESET_PASSWORD_TOKEN_SECRET||RESET_PASSWORD_TOKEN_SECRET|
|VERIFICATION_TOKEN_SECRET||VERIFICATION_TOKEN_SECRET|

### Значения POSTGRES_DSN для .env 
| Поле | Назначение |
|----- |-------|
| user | логин |
| pass | пароль|
| localhost | IP |
| 5432 | Порт |
| footbar | название БД |
## Запуск
uvicorn app.app:app --port 5020 --reload
# Если через docker
## Building 
`docker build -t "users" .`
## Запуск
Для запуска перейдите в папку `deploy` и проследуйте инструкциям
## Документация
Documentation: `http://localhost:5020/docs`


## Api
| Method | Route           | Description        |
|--------|-----------------|--------------------|
| POST | `groups/` | Create new group |
| GET | `groups/` | Get all groups |
| GET | `groups/{GroupID}` | Get group by ID |
| PUT | `groups/{GroupID}` | Update group by ID |
| DELETE | `groups/{GroupID}` | delete group by ID |
