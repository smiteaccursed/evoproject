## DEPLOY
# Настройка и запуск
1. Создайте `.env` файл в текущей директории
2. Заполните поля в нем
```ini
POSTGRES_PASSWORD=пароль
POSTGRES_USER=логин
POSTGRES_DB=название БД
PG_DSN=postgresql://логин:пароль@Локальный IP адресс:порт/название БД
```
3. Настройка `docker-compose.yaml` при необходимости
4. Для запуска
```ini
docker-compose up 
```
6. Для завершения
```ini
docker-compose down
```
7. Используйте `localhost:5000` для доступа
