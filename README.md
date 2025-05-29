# FastAPI Todo App

This is a simple todo application built with FastAPI.

## Installation

```bash
pip install -r requirements.txt
```

## Running

```bash
uvicorn main:app --reload
```

## Project Structure

```
├── main.py        # FastAPI entrypoint
├── requirements.txt
├── app
│   ├── __init__.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── database.py
│   └── routers
│       ├── __init__.py
│       └── tasks.py
└── .gitignore
``` 

# Создание тестовой базы
Создается докер контейнер в котором будет развернута база постгреса

- пароль 12345

```bash
docker run --name local-pg -e POSTGRES_PASSWORD=12345 -d postgres
```