.PHONY: build up down logs test lint format clean help migrate shell superuser

# Variables
DOCKER_COMPOSE = docker-compose
DOCKER_EXEC = $(DOCKER_COMPOSE) exec web
PYTHON_MANAGE = python manage.py

help:
	@echo "Available commands:"
	@echo "build      - Build Docker images"
	@echo "up         - Start Docker containers"
	@echo "down       - Stop Docker containers"
	@echo "logs       - View Docker container logs"
	@echo "test       - Run tests"
	@echo "lint       - Run flake8 linting"
	@echo "format     - Format code with black"
	@echo "clean      - Remove Python compiled files and cache"
	@echo "migrate    - Run Django migrations"
	@echo "shell      - Open Django shell"
	@echo "superuser  - Create Django superuser"

build:
	$(DOCKER_COMPOSE) build

up:
	$(DOCKER_COMPOSE) up -d

down:
	$(DOCKER_COMPOSE) down

logs:
	$(DOCKER_COMPOSE) logs -f

test:
	$(DOCKER_EXEC) pytest

lint:
	$(DOCKER_EXEC) flake8 .

format:
	$(DOCKER_EXEC) black .

clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	find . -type f -name ".coverage" -delete
	find . -type d -name "*.egg-info" -exec rm -r {} +
	find . -type d -name "*.egg" -exec rm -r {} +
	find . -type d -name ".pytest_cache" -exec rm -r {} +
	find . -type d -name ".coverage" -exec rm -r {} +
	find . -type d -name "htmlcov" -exec rm -r {} +

migrate:
	$(DOCKER_EXEC) $(PYTHON_MANAGE) migrate

shell:
	$(DOCKER_EXEC) $(PYTHON_MANAGE) shell

superuser:
	$(DOCKER_EXEC) $(PYTHON_MANAGE) createsuperuser

# Development shortcuts
dev-setup: build up migrate

dev-reset: down clean dev-setup

# Testing shortcuts
test-coverage:
	$(DOCKER_EXEC) pytest --cov=todo_app --cov-report=html

# Database shortcuts
db-flush:
	$(DOCKER_EXEC) $(PYTHON_MANAGE) flush --no-input

db-reset: down
	rm -f todo_app/db.sqlite3
	make dev-setup

# Dependency management
requirements:
	$(DOCKER_EXEC) pip freeze > requirements.txt
