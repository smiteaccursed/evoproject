# Севрис проверки полномочий
## Описание
Сервис позволяет работать с жалобами и отправляет уведомление при добавлении новых
## API
| Method | Route           | Description        |
|--------|-----------------|--------------------|
| POST   | `/complaints/`       | Add new complaint and send message to rabbitmq      |
| GET    | `/complaints/by_status/{status}` | Get complaints by status    |
| PUT    | `/complaints/{CID}` | Update complaint's status by ID |
| GET    | `/complaints/{CID}` | Get complaint by ID    |
| GET    | `/complaints/user/{userID}` | Get complaints about the user    |
## Запуск
### Установка
- Установка зависимостей: `pip install -r requirements.txt `
- Подготовка .env файла: 
```
MONGO_DSN=mongodb://report:report@26.255.132.24:27017/complaint
RABBITMQ_DSN=amqp://guest:guest@127.0.0.1:5672//
```
### Запуск
uvicorn app.app:app --port 5030 --reload
### Если через docker
`docker build -t "complaint" .`
