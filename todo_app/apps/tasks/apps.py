# todo_app/apps/tasks/apps.py
from django.apps import AppConfig


class TasksConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "todo_app.apps.tasks"