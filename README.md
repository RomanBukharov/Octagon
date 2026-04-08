# Octagon - project

У меня мак, поэтому часть с WSL пропустил.

## Запуск API

#### Установить зависимости:
```bash
pip install -r requirements.txt
```
### Убедиться, что PostgreSQL запущен и .env заполнен правильно.

### Запустить API из корня проекта:
```bash
uvicorn app.main:app --reload
```
### Открыть:
Swagger: http://127.0.0.1:8000/docs
Health-check: http://127.0.0.1:8000/health