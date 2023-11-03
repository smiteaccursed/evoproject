# Telegram service
# Если без докера
### Установка
- Установка зависимостей: `pip install -r requirements.txt `
- Подготовка .env файла:
```
TELEGRAM_CHAT_IDS = [YOUR_ID]
TELEGRAM_BOT_TOKEN = YOUR_TOKEN
RABBITMQ_DSN=amqp://admin:admin@127.0.0.1:5672//
```
Готовый токен = `6528915216:AAEBv-O5X1itJWQD0YDAwHfNpC_BHPkPbJk`
### Запуск с использование файла конфигурации .env

Для запуска из файла конфигурации нужно поместить файл .env в корень сервиса

### Конфигурация
| Переменная    | Назначение                      | Значение по-умолчанию                        |
| -----------   | -----                           | ---                                          |
|TELEGRAM_CHAT_IDS | ID пользователей в виде списка. Получить можно, используя любого бота в телеграме |[ID]|
|TELEGRAM_BOT_TOKEN|Токен бота. Можно получить от Bot Father|TELEGRAM_BOT_TOKEN|
|RABBITMQ_DSN| URL ссылка. Предварительно установите RabbitMQ, и запустите плагины|amqp://admin:admin@127.0.0.1:5672//|


## Запуск
app/app.py
# Если через docker
## Building 
`docker build -t "telegram-service .`
## Запуск
Для запуска перейдите в папку `deploy` и проследуйте инструкциям
## Документация
Documentation: `http://localhost:5050/docs`
