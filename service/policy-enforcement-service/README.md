# Policy service
# Если без докера
### Установка
- Установка зависимостей: `pip install -r requirements.txt `
- Подготовка .env файла:
- `JWT_SECRET=JWT_SECRET`
- `POLICIES_CONFIG_PATH=policies.yaml`

### Запуск с использование файла конфигурации .env

Для запуска из файла конфигурации нужно поместить файл .env в корень сервиса

### Конфигурация
| Переменная    | Назначение                      | Значение по-умолчанию                        |
| -----------   | -----                           | ---                                          |
|JWT_SECRET ||JWT_SECRET|
|POLICIES_CONFIG_PATH||policies.yaml|


## Запуск
uvicorn app.app:app --port 5100 --reload
# Если через docker
## Building 
`docker build -t "policy .`
## Запуск
Для запуска перейдите в папку `deploy` и проследуйте инструкциям
## Документация
Documentation: `http://localhost:5100/docs`
