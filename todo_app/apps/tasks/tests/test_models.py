import pytest
from todo_app.apps.tasks.models.task import Task


@pytest.mark.django_db
class TestTaskModel:
    def test_create_task(self):
        task = Task.objects.create(
            title="Test Task", description="Test Description", completed=False
        )
        assert task.title == "Test Task"
        assert task.description == "Test Description"
        assert task.completed is False
