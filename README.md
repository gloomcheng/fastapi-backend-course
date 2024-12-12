# Backend Development Course using FastAPI

This is a course example project based on FastAPI with database integration and other essential features. This project aims to help learners understand how to build a complete FastAPI application.

## Dependencies

This project uses the following key packages:

- **FastAPI**: Modern, fast web framework for building APIs with Python
  - High performance, easy to use, and fully compatible with OpenAPI (Swagger) and JSON Schema
  - Used for creating REST APIs with automatic documentation

- **SQLAlchemy**: SQL toolkit and ORM
  - Provides a full suite of well-known enterprise-level persistence patterns
  - Used for database operations and model definitions

- **Alembic**: Database migration tool
  - Handles database schema changes and version control
  - Recommended over `Base.metadata.create_all()` for proper migration management

- **Pydantic**: Data validation using Python type annotations
  - Enforces type hints at runtime and provides user-friendly errors
  - Used for request/response models and configuration management

- **Python-jose**: JavaScript Object Signing and Encryption implementation
  - Provides JWT token handling capabilities
  - Used for authentication and authorization

- **Passlib**: Password hashing library
  - Handles secure password storage
  - Used for user authentication

## Setup and Installation

1. Install pipenv if you haven't already:
```bash
pip install -U pipenv
```

2. Install project dependencies and create a virtual environment:
```bash
pipenv install
```

### About Virtual Environments

A virtual environment is an isolated Python environment that keeps project dependencies separate from your system Python installation. When you use pipenv:

- It creates a dedicated virtual environment for your project
- Manages project-specific dependencies without affecting other projects
- Ensures consistent development environments across different machines
- Prevents conflicts between different projects' package versions
- Makes it easier to track and reproduce your project's exact environment

To activate the virtual environment:
```bash
pipenv shell
```

## Important Notes

### Database Migrations

⚠️ **Warning**: Do not use `Base.metadata.create_all(bind=engine)` for database schema management. Here's why:

- When you modify `models.py` or configure `env.py`, the server will automatically create the database before you attempt to add a new migration version
- This prevents Alembic from properly generating `create_table` and other migration commands
- The automatically created database structure may become out of sync with migration history

Instead, use Alembic for database migrations:
```bash
# Generate migration
pipenv run alembic revision --autogenerate -m "description"

# Apply migration
pipenv run alembic upgrade head
```

### Start FastAPI

```
$ pipenv run fastapi dev app/main.py
```

## **Contact**
For questions or suggestions, please reach out via Issues or email at [gloomcheng@gmail.com](mailto:gloomcheng@gmail.com).