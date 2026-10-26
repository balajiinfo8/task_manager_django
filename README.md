# ⚡ TaskForge — Task Management Platform

A Django-powered task management application built to demonstrate practical backend development, user authentication, database operations, and secure task management. TaskForge follows Django's Model–View–Template (MVT) architecture and provides a foundation for building more advanced productivity applications.

## 🔗 Live Demo

👉 [Launch TaskForge](https://task-manager-django-iqs0.onrender.com)

## 🛠️ Tech Stack

- **Language:** Python
- **Backend Framework:** Django
- **API Framework:** Django REST Framework
- **Authentication:** Django sessions and JWT authentication endpoints
- **Database:** SQLite for local development
- **Frontend:** HTML, CSS, Bootstrap
- **Forms:** Django Forms and Crispy Forms
- **Deployment:** Render
- **Version Control:** Git and GitHub

## ✨ Key Features

- 🔐 **User Authentication** — Registration, login, and logout.
- 📝 **Task Management** — Create, view, update, and delete tasks.
- 👤 **User-Specific Tasks** — Support for associating tasks with their owners.
- 🗃️ **Database Operations** — Interact with application data through the Django ORM.
- 🛡️ **Request Protection** — Django authentication decorators and CSRF protection for applicable form submissions.
- 🎨 **Responsive Interface** — Bootstrap-based pages for task management.
- 🔑 **JWT Endpoints** — Token generation and refresh endpoints for API authentication, where configured.

## 🏗️ Backend Architecture

TaskForge uses Django's Model–View–Template (MVT) architecture to separate data management, application logic, routing, and presentation.

| Component | Responsibility |
|---|---|
| **Models** | Define application data and database relationships |
| **Views** | Process HTTP requests and implement application logic |
| **URL Configuration** | Route requests to the appropriate views |
| **Forms** | Handle user input and validation |
| **Templates** | Render the user interface |
| **Django ORM** | Query and update database records |
| **Authentication** | Manage user identity and session-based access |

### Request Lifecycle

1. A user sends an HTTP request from the browser.
2. Django resolves the requested URL.
3. The matching view processes the request.
4. The view validates input and interacts with the database when necessary.
5. Django returns the appropriate response, such as a rendered HTML page or redirect.

## 📍 Application Routes

| Route | Description |
|---|---|
| `/` | Login page |
| `/register/` | User registration |
| `/home/` | Task dashboard |
| `/logout/` | Logout |
| `/del/<item_id>/` | Delete a task |
| `/edit/<item_id>/` | Edit a task |
| `/api/token/` | Obtain JWT tokens |
| `/api/token/refresh/` | Refresh an access token |

*Note: Confirm these paths against the current Django URL configuration before relying on them; route availability depends on the implementation.*

## 🚀 Getting Started

Follow these steps to run TaskForge locally.

### Prerequisites

- Python 3.12 or a compatible version
- Git
- A terminal such as PowerShell, Command Prompt, or Bash

### 1. Clone the Repository

```bash
git clone https://github.com/balajiinfo8/task_manager_django.git
cd task_manager_django
```

### 2. Create a Virtual Environment

**Windows PowerShell:**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Linux / macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Apply Database Migrations

```bash
python manage.py migrate
```

### 5. Check the Configuration

```bash
python manage.py check
```

### 6. Start the Development Server

```bash
python manage.py runserver
```

Open the application in your browser:

**http://127.0.0.1:8000/**

## 🧪 Useful Development Commands

| Command | Purpose |
|---|---|
| `python manage.py check` | Check the Django project configuration |
| `python manage.py makemigrations` | Generate migration files for model changes |
| `python manage.py migrate` | Apply database migrations |
| `python manage.py test` | Run automated tests |
| `python manage.py createsuperuser` | Create an administrative account |

## 🔒 Security and Deployment Considerations

For a deployment intended for public use:

- Keep `SECRET_KEY` and other sensitive credentials in environment variables.
- Set `DEBUG=False` in production.
- Configure `ALLOWED_HOSTS` and `CSRF_TRUSTED_ORIGINS` correctly.
- Ensure users can access or modify only their own tasks.
- Validate submitted data on the server.
- Use HTTPS and secure cookie settings in production.
- Configure static files and a suitable persistent database for the hosting environment.
- Test authentication, permissions, and error handling before release.

## 🔮 Future Enhancements

- Expand automated tests for authentication, task ownership, and CRUD operations.
- Build a comprehensive REST API with Django REST Framework.
- Add API documentation using Swagger/OpenAPI.
- Implement task search, filtering, sorting, and pagination.
- Add task deadlines, reminders, and notifications.
- Introduce team-based permissions and role management.
- Add Docker-based development and deployment.
- Configure PostgreSQL for environments requiring a production database.

## 👨‍💻 Author

**Balaji V**  
Python Backend Developer

- **GitHub:** [balajiinfo8](https://github.com/balajiinfo8)
- **LinkedIn:** [Balaji Vinothkumar](https://www.linkedin.com/in/balaji-vinothkumar/)

---

*TaskForge is a practical project for exploring Django backend development, authentication, ORM operations, application structure, and deployment practices.*
