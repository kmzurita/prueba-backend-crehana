# Todo List API with GraphQL and Django REST Framework

This app was developed as part of the backend developer test for Crehana 

## Features

- GraphQL API using Strawberry
- REST API using Django REST Framework
- Comprehensive test suite
- Docker support
- Code formatting with Black
- Code linting with Flake8

## Requirements

- Python 3.8+
- Docker (optional)
- pip

## Local Variables

Copy and change the file .env.example to a .env file. Generate a new django key to replace ```SECRET_KEY = your-django-insecure-secret-key```

## Quick Start with Docker

1. Clone the repository:
```bash
git clone <repository-url>
cd todo-project
```

2. Start the development environment:
```bash
make dev-setup
```

This command will:
- Build Docker images
- Start containers
- Run migrations

The API will be available at http://localhost:8000

## Available Make Commands

### Development Commands
```bash
make build          # Build Docker images
make up             # Start Docker containers
make down           # Stop Docker containers
make logs           # View Docker container logs
make dev-setup      # Complete setup: build, up, and migrate
make dev-reset      # Reset development environment
```

### Database Commands
```bash
make migrate        # Run Django migrations
make db-flush       # Flush database
make db-reset       # Reset database completely
make superuser      # Create superuser
```

### Testing and Code Quality
```bash
make test          # Run tests
make test-coverage # Run tests with coverage report
make lint          # Run flake8 linting
make format        # Format code with black
```

### Utility Commands
```bash
make shell         # Open Django shell
make clean         # Remove Python compiled files and cache
make requirements  # Update requirements.txt
```

### Help
```bash
make help          # Show all available commands
```

## Local Development Setup (Alternative)

If you prefer to develop without Docker:

1. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run migrations:
```bash
python manage.py migrate
```

4. Start the development server:
```bash
python manage.py runserver
```


## API Documentation

### GraphQL Endpoints

GraphQL endpoint: `/graphql/`

#### Query Examples

Get all tasks:
```graphql
query {
  tasks {
    id
    title
    description
    completed
  }
}
```

Get single task:
```graphql
query {
  task(id: 1) {
    title
    description
    completed
  }
}
```

#### Mutation Examples

Create task:
```graphql
mutation {
  createTask(
    title: "New Task"
    description: "Task Description"
    completed: false
  ) {
    id
    title
    description
    completed
  }
}
```

Update task:
```graphql
mutation {
  updateTask(
    id: 1
    title: "Updated Task"
    completed: true
  ) {
    id
    title
    completed
  }
}
```

Delete task:
```graphql
mutation {
  deleteTask(id: 1)
}
```

### REST API Endpoints

- `GET /api/tasks/` - List all tasks
- `POST /api/tasks/` - Create a new task
- `GET /api/tasks/{id}/` - Retrieve a task
- `PUT /api/tasks/{id}/` - Update a task
- `PATCH /api/tasks/{id}/` - Partially update a task
- `DELETE /api/tasks/{id}/` - Delete a task

## Testing

Run all tests:
```bash
pytest
```

Run tests with coverage report:
```bash
pytest --cov=todo_app --cov-report=html
```

## Code Quality

Format code with Black:
```bash
black .
```

Run Flake8 linting:
```bash
flake8
```

## Project Structure

```
todo_project/
├── .env.example
├── .flake8
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── manage.py
├── pytest.ini
├── README.md
├── requirements.txt
└── todo_app/
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    ├── wsgi.py
    └── apps/
        ├── __init__.py
        └── tasks/
            └── migrations/
                ├── __init__.py
                ├── any_mygration.py
            └── models/
                ├── __init__.py
                ├── task.py
            └── mutations/
                ├── __init__.py
                ├── task_mutations.py
            └── schemas/
                ├── __init__.py
                ├── task_schema.py   
                ├── task_type.py
            └── serializers/
                ├── __init__.py
                ├── task_serializer.py
            └── tests/
                ├── __init__.py
                ├── conftest.py
                ├── test_models.py
                ├── test_mutations.py
                ├── test_queries.py
            └── views/
                ├── __init__.py
                ├── task_view.py
            ├── __init__.py
            ├── admin.py
            ├── apps.py
            ├── urls.py
```
