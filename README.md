# KanMind Backend

A backend project for Kanban boards and task management, based on Django and Django REST Framework.

## Features

- User management with custom User model
- Token-based authentication
- REST API for Boards, Tasks, and Users
- CORS support (open to all origins for development)

## Prerequisites

- Python 3.10 or higher
- [pip](https://pip.pypa.io/en/stable/)
- (Optional) Virtual environment (recommended)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Ay010/kanmind-backend.git
   cd kanmind-backend
   ```
2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # Linux/macOS:
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

- The main settings are located in `kanmind/settings.py`.
- For production use, sensitive data (such as `SECRET_KEY`) should be moved to a `.env` file (e.g., using [django-environ](https://django-environ.readthedocs.io/en/latest/)).
- SQLite is used as the default database. For other databases, please adjust the settings in `settings.py`.

## Migrations & Superuser

1. Apply migrations:
   ```bash
   python manage.py migrate
   ```
2. Create superuser:
   ```bash
   python manage.py createsuperuser
   ```

## Starting the Project

```bash
python manage.py runserver
```

The backend will be available at: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## API Authentication

- The API uses token authentication.
- After login, the user receives a token that must be included in subsequent API requests in the header `Authorization: Token <token>`.

## Special Features & Notes

- **CORS:** For development, CORS is allowed for all origins. In production, please restrict to specific domains!
- **User Model:** A custom User model is used (`user_auth.User`).
- **Default Permissions:** All API endpoints are only accessible to authenticated users.
- **Database:** The `db.sqlite3` file is in `.gitignore` and is not included in the repository.

## Example: Obtaining a Token

```bash
POST /user_auth/api/token/
{
  "username": "<your_username>",
  "password": "<your_password>"
}
```

Response:

```json
{
  "token": "<your_token>"
}
```

## Further Links

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)

---

**Questions or Issues?**
Please create an issue in the [GitHub Repository](https://github.com/Ay010/kanmind-backend).
