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

## Team Collaboration Strategy

This section outlines the division of responsibilities, task dependencies, and
communication expectations for developing the Libra Library Management System.
The goal is for every team member to make a meaningful contribution while
understanding how their work connects to the rest of the application.

### 1. Task Allocation and Responsibilities

#### Tim – Project Lead

**Foundation and integration**

- Maintain the existing Django project configuration.
- Manage project-level URLs and template settings.
- Maintain `base.html` and shared navigation.
- Coordinate implementation and ensure components work together.
- Maintain the shared project and merge completed team changes.
- Oversee application integration and testing.

**Learning objectives:** Django project architecture, URL routing, template
inheritance, application integration, and project coordination.

**Communication requirements**

- Communicate with all members to understand progress and identify integration
  issues.
- Coordinate with Edith, Ronald, Dalton, and Beatrice regarding their view
  functions, URL patterns, and template requirements.
- Coordinate with Shan on the existing `Book` model and any required model
  adjustments.

#### Shan – Database Management and Django Admin

- Review and understand the existing `Book` model in `core/models.py`.
- Configure the `Book` model in `core/admin.py`.
- Customise Django Admin list displays.
- Implement admin search fields and availability filters.
- Test database operations using the Django ORM.
- Prepare sample book records for application testing.
- Verify model constraints and database behaviour.

**Learning objectives:** Django ORM, database querying, Django Admin
customisation, model validation, and database management.

**Communication requirements**

- Communicate with Tim regarding the existing model and any proposed changes.
- Coordinate with Edith and Dalton if changes to model fields or validation
  affect their forms.
- Coordinate with Ronald and Beatrice when preparing records for testing
  listing and deletion functionality.

#### Edith – CRUD: Create

- Create `BookForm` in `core/forms.py`.
- Implement the book registration view.
- Handle GET and POST requests.
- Validate submitted book information.
- Save valid records to the database.
- Create `book_form.html` using Bootstrap.
- Display form errors and success messages.

**Learning objectives:** Django ModelForms, form validation, POST requests, CSRF
protection, saving records, and template rendering.

**Communication requirements**

- Communicate with Tim to agree on the registration URL and view naming
  conventions.
- Coordinate with Shan to understand the existing `Book` model fields and
  validation requirements.
- Communicate with Dalton to ensure the form can also support updating
  existing books.
- Coordinate with Ronald to ensure newly registered books appear correctly in
  the listing.

#### Ronald – CRUD: Read

- Implement the book listing and individual book details views.
- Retrieve book records using Django QuerySets.
- Create `book_list.html` and `book_detail.html`.
- Display book information and availability status.
- Implement basic book search by title or author.

**Learning objectives:** Django ORM, QuerySets, retrieving records, context
dictionaries, dynamic templates, and search functionality.

**Communication requirements**

- Communicate with Shan to understand the `Book` model fields.
- Coordinate with Edith to ensure newly created books appear in the listing.
- Coordinate with Dalton to ensure updated book information is reflected
  correctly.
- Coordinate with Beatrice to ensure deleted books no longer appear in the
  listing.
- Communicate with Tim regarding URL patterns and template integration.

#### Dalton – CRUD: Update

- Implement the book update view.
- Reuse the `BookForm` created by Edith.
- Retrieve existing book records for editing.
- Handle GET and POST requests.
- Populate forms with existing book information and save updates.
- Ensure book availability can be modified.
- Create or adapt the editing template.

**Learning objectives:** `get_object_or_404()`, instance-based ModelForms,
updating database records, HTTP requests, and redirects.

**Communication requirements**

- Coordinate with Edith to reuse `BookForm` and agree on its fields and
  validation.
- Communicate with Shan regarding the `Book` model and its constraints.
- Coordinate with Ronald to ensure updated information appears correctly in
  book listings and details.
- Communicate with Tim regarding URL patterns and template integration.

#### Beatrice – CRUD: Delete

- Implement the book deletion view.
- Retrieve the selected book record.
- Create `book_confirm_delete.html`.
- Implement deletion confirmation.
- Handle deletion through POST requests.
- Display appropriate success messages.
- Test deletion behaviour and redirects.

**Learning objectives:** Object retrieval, Django deletion operations, HTTP
POST requests, confirmation templates, redirects, and user feedback.

**Communication requirements**

- Coordinate with Ronald to ensure deleted books are removed from the listing
  and cannot be accessed through their previous detail links.
- Communicate with Tim regarding URL patterns and template integration.
- Coordinate with Shan when preparing test records for deletion.

### 2. Task Dependencies and Collaboration Flow

| Task | Depends on / requires coordination with |
|---|---|
| Database and Admin | Tim – existing project and `Book` model |
| Book registration | Shan – model; Tim – URL conventions |
| Book listing and details | Shan – model; Tim – URL conventions |
| Book updating | Edith – shared `BookForm`; Shan – model |
| Book deletion | Shan – model; Ronald – listing and details integration |
| Final integration | All members – working components and agreed interfaces |

#### Recommended implementation sequence

1. **Foundation:** Tim provides the existing project structure and confirms the
   model interface with Shan.
2. **Database preparation:** Shan verifies the model and configures Django
   Admin.
3. **Form development:** Edith creates the shared `BookForm` and coordinates
   its use with Dalton.
4. **CRUD implementation:** Edith, Ronald, Dalton, and Beatrice implement their
   respective functionality.
5. **Cross-component integration:** Members verify that creating, viewing,
   updating, and deleting books work together.
6. **Final testing:** All members test the complete application and report
   issues to Tim.

### 3. Shared Learning and Collaboration

Each member has a primary area of responsibility, but the assignments are not
intended to limit anyone to learning only that area. Keep ownership clear while
using collaboration to gain experience with the wider Django application.

- Pair with the owner of a related task when working across dependencies, such
  as Edith and Dalton aligning on the shared `BookForm`.
- Rotate peer reviews so members review code outside their primary area and
  learn how the pieces fit together.
- Have each member demonstrate their feature and explain how its view, model,
  URL, and template work together.
- During integration and final testing, have everyone run and test the complete
  create, read, update, and delete flows.
- Share questions and findings so that implementation knowledge is not limited
  to the person who wrote a particular component.
- Tim remains responsible for maintaining the shared project and merging
  completed changes; feature owners should communicate and resolve issues
  before asking for integration.

### 4. Communication Expectations

- Communicate with the relevant team member whenever your implementation
  depends on their work.
- Agree on model fields, form names, view names, and URL patterns before
  depending on them.
- Do not independently change shared components without informing the affected
  members.
- If a dependency is not ready, communicate early rather than waiting until
  the deadline.
- Test your functionality alongside the components it interacts with.
- Ask questions and assist one another where necessary.

> **The objective is collaborative development.** Each member owns a
> component, but the success of the application depends on everyone
> understanding and supporting how those components work together.
