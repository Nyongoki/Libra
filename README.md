# Libra Library Management System

## Assignment overview

Libra is a Django assignment for a team of six students. The project provides a
basic library management interface for registering and maintaining book records.
Team members should coordinate ownership of the application areas below and work
in separate branches to avoid overwriting one another's changes.

## Current project structure

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
`-- core/
    |-- migrations/
    |-- admin.py
    |-- apps.py
    |-- models.py
    |-- tests.py
    `-- views.py
```

The Django project settings package is named `config`. The starter application
is named `core`.

## Planned assignment structure

The team may organize the application or rename `core` to `books` when that work
is assigned. A conventional target structure is:

```text
library_management/
|-- manage.py
|-- library_management/
|   |-- settings.py
|   |-- urls.py
|   `-- wsgi.py
|-- books/
|   |-- migrations/
|   |-- models.py
|   |-- forms.py
|   |-- views.py
|   |-- urls.py
|   `-- admin.py
|-- templates/
|   |-- base.html
|   |-- dashboard.html
|   |-- book_list.html
|   |-- book_detail.html
|   |-- book_form.html
|   `-- book_confirm_delete.html
`-- static/
    `-- css/
        `-- style.css
```

Names in the planned structure describe the intended feature layout and may
match the actual `config` and `core` names while implementation work is in
progress.

## Scope coverage

| Feature | Expected behavior |
|---|---|
| Register books | Add a new book to the database |
| View books | Display all registered books |
| View details | Display information for an individual book |
| Update books | Edit existing book information |
| Delete books | Remove a book record |
| Availability | Mark a book as Available or Borrowed |

## Book model

The starter `Book` model contains:

- Title
- Author
- ISBN
- Category
- Publication year
- Availability (`available` or `borrowed`)
- Creation timestamp
- Update timestamp

The model is currently defined in `core/models.py`. Database migrations have
not been created or run as part of the starter assignment setup.

## Team workspace

- Use focused branches for individual feature areas.
- Keep migrations and database files out of team commits unless the team agrees
  otherwise.
- Add tests for model validation and each CRUD workflow.
- Coordinate shared files such as settings, URLs, templates, and stylesheets.

## Setup

Create and activate a virtual environment, install dependencies, and start the
development server with:

```powershell
python -m pip install -r requirements.txt
python manage.py runserver
```
