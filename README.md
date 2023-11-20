# Проект "Книжный форум"
![эвопроект drawio](https://github.com/smiteaccursed/evoproject/assets/144155604/da8e4b2c-bb66-4697-8819-4cbbd9a02123)
## Сервисы 
| Название сервиса | Переход |
| --- | --- |
| Complaint service| [Перейти](/services/complaint-service)
| Forum service | [Перейти](/services/forum-service/)
| Library service | [Перейти](/services/library-service/)
| Policy enforcement service | [Перейти](/services/policy-enforcement-service/)
| Telegram service | [Перейти](/services/telegram-service/)
| User service | [Перейти](/services/user-service/)

## Тесты
| Тест | Переход |
| --- | --- |
| E2e test| [Перейти](/tests/)
| Library service test | [Перейти](/services/library-service/unit-test/)
## Проверка уязвимостей

### Уязвимости сервиса
1) Установить bandit:
```sh
pip install bandit
```
2) Перейти в папку сервиса
3) Запустить проверку
```sh
python -m bandit -r ./app
```
### Уязвимости образа
1) Установить расширение Trivy для Docker Desktop
2) Выбрать образ и запустить сканирование
