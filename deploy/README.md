# DEPLOY
## Настройка и запуск
1. Создайте `.env` файл в текущей директории
2. Заполните поля в нем
```ini
POSTGRES_PASSWORD=пароль
POSTGRES_USER=логин
POSTGRES_DB=название БД
PG_DSN=postgresql://логин:пароль@Локальный IP адресс:порт/название БД
MONGO_USER=логин
MONGO_DB=название
MONGO_PASSWORD=пароль
MONGO_DSN=mongodb://логин:пароль@Локальный IP адресс:порт/название БД
JWT_SECRET=JWT_SECRET
RESET_PASSWORD_TOKEN_SECRET=RESET_PASSWORD_TOKEN_SECRET
VERIFICATION_TOKEN_SECRET=VERIFICATION_TOKEN_SECRET
PG_ADSN=postgresql+asyncpg://логин:пароль@Локальный IP адресс:порт/название БД
POLICIES_CONFIG_PATH=/mnt/policies.yaml

```
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
