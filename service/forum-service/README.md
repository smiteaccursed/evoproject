# Forum service
Сервис форума, позволяет хранить и работать с топиками и сообщениями в них
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
uvicorn app.app:app --port 5010 --reload
# Если через docker
## Building 
`docker build -t "forum" .`
## Запуск
Для запуска перейдите в папку `deploy` и проследуйте инструкциям
## Документация
Documentation: `http://localhost:5000/docs`

## Api
| Method | Route           | Description        |
|--------|-----------------|--------------------|
|GET|/topics/|get all topics|
|GET|/topic/{topicID}|get topic by ID|
|DELETE|/topic/{topicID}|delete topic by ID|
|PUT|/topic/{topicID}|update topic by ID|
|POST|/topic/|add topic|
|POST|/topic/{topicID}/message/|add message|
|GET|/message/{messageID}|get message by ID|
|PUT|/message/{messageID}|update message by ID|
