# DEPLOY
## Настройка и запуск
1. Создайте `.env` файл в текущей директории
2. Заполните поля в нем
```ini
POSTGRES_PASSWORD=userpass
POSTGRES_USER=user
POSTGRES_DB=dbname
PG_DSN=postgresql://user:userpass@localhost:port/dbname
MONGO_USER=mongouser
MONGO_DB=mongoname
MONGO_PASSWORD=mongopass
MONGO_DSN=mongodb://mongouser:mongopass@localhost:port/mongoname
JWT_SECRET=JWT_SECRET
RESET_PASSWORD_TOKEN_SECRET=RESET_PASSWORD_TOKEN_SECRET
VERIFICATION_TOKEN_SECRET=VERIFICATION_TOKEN_SECRET
PG_ADSN=postgresql+asyncpg://user:userpass@localhost:port/dbname
POLICIES_CONFIG_PATH=/mnt/policies.yaml
RABBITMQ_DEFAULT_USER=admin
RABBITMQ_DEFAULT_PASS=pass
RABBITMQ_DSN=amqp://admin:pass@rabbitmq:5672/
TELEGRAM_CHAT_IDS=[YOUR_ID]
TELEGRAM_BOT_TOKEN=TOKER
```
Готовый токен телеграм бота `6528915216:AAEBv-O5X1itJWQD0YDAwHfNpC_BHPkPbJk ` 

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
