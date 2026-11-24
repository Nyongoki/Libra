# Libra Library Management System

Libra is a Django library management application for registering, viewing,
updating, and deleting books.

## Project structure

```text
Libra/
|-- manage.py
|-- requirements.txt
|-- README.md
|-- config/
|   |-- settings.py
|   |-- urls.py
|   |-- wsgi.py
|   `-- asgi.py
|-- core/
|   |-- migrations/
|   |-- admin.py
|   |-- apps.py
|   |-- models.py
|   |-- tests.py
|   `-- views.py
|-- templates/
|   `-- core/
|-- static/
|   `-- css/
|       `-- style.css
`-- db.sqlite3
```

The Django settings package is `config`, and the application is `core`.

## Core functionality

| Feature | Expected behaviour |
|---|---|
| Register books | Add new books to the database |
| View books | Display all registered books |
| View details | Display information for an individual book |
| Update books | Edit existing book information |
| Delete books | Remove book records |
| Availability | Mark books as Available or Borrowed |

## Book model

The `Book` model in `core/models.py` contains:

- `title`: maximum length of 200 characters
- `author`: maximum length of 150 characters
- `isbn`: maximum length of 20 characters, unique
- `category`: maximum length of 100 characters
- `publication_year`: positive integer
- `availability`: `available` or `borrowed`
- `created_at`: creation timestamp
- `updated_at`: update timestamp

## Setup

```powershell
python -m pip install -r requirements.txt
python manage.py runserver
```
