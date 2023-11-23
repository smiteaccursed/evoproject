# DEPLOY
## Настройка и запуск
1. Создайте `.env` файл в текущей директории
2. Заполните поля в нем
```ini
POSTGRES_PASSWORD=admin
POSTGRES_USER=adminpass
POSTGRES_DB=pgdb
PG_DSN=postgresql://admin:adminpass@postgresql:5432/pgdb
PG_ADSN=postgresql+asyncpg://admin:adminpass@postgresql:5432/pgdb

MONGO_USER=report
MONGO_DB=complaint
MONGO_PASSWORD=report
MONGO_DSN=mongodb://report:report@mongo:27017/complaint

JWT_SECRET=JWT_SECRET
RESET_PASSWORD_TOKEN_SECRET=RESET_PASSWORD_TOKEN_SECRET
VERIFICATION_TOKEN_SECRET=VERIFICATION_TOKEN_SECRET

POLICIES_CONFIG_PATH=/mnt/policies.yaml

RABBITMQ_DEFAULT_USER=guest
RABBITMQ_DEFAULT_PASS=guest
RABBITMQ_DSN=amqp://guest:guest@rabbitmq:5672/

TELEGRAM_CHAT_IDS=["YOUR ID"]
TELEGRAM_BOT_TOKEN="BOT TOKEN"

DEFAULT_GROUPS_CONFIG_PATH=/mnt/default-groups.json

```
## Поля, необходимые для заполнения вручную
| Переменная    | Назначение                      | Получение                        |
| -----------   | -----                           | ---                                          |
| TELEGRAM_CHAT_IDS  | ID телеграмм чата | Воспользоваться любым ботом для получения ID в телеграме |
| TELEGRAM_BOT_TOKEN | Токен телеграмм бота| Воспользоваться ботом BotFather в телеграме|

3. Настройка `docker-compose.yaml` при необходимости
4. Для запуска
```ini
docker-compose up --build
```
6. Для завершения
```ini
docker-compose down
```
7. Используйте `localhost и порт, который указан в docker-compose файле` для доступа
