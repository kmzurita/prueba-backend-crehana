import pytest
from django.test import Client
import json
from todo_app.apps.tasks.models.task import Task


@pytest.mark.django_db
class TestTaskQueries:
    def setup_method(self):
        self.client = Client()
        self.task = Task.objects.create(
            title="Test Task", description="Test Description", completed=False
        )

    def test_get_tasks(self):
        query = """
        {
            tasks {
                id
                title
                description
                completed
            }
        }
        """
        response = self.client.post(
            "/graphql/",
            data=json.dumps({"query": query}),
            content_type="application/json",
        )

        assert response.status_code == 200
        data = json.loads(response.content)
        assert "errors" not in data
        assert "data" in data
        assert "tasks" in data["data"]
