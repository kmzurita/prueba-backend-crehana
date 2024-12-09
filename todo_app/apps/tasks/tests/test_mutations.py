import pytest
from django.test import Client
import json


@pytest.mark.django_db
class TestTaskMutations:
    def setup_method(self):
        self.client = Client()

    def test_create_task(self):
        mutation = """
        mutation {
            createTask(
                title: "Test Task"
                description: "Test Description"
            ) {
                id
                title
                description
                completed
            }
        }
        """
        response = self.client.post(
            "/graphql/",
            data=json.dumps({"query": mutation}),
            content_type="application/json",
        )

        assert response.status_code == 200
        data = json.loads(response.content)
        assert "errors" not in data
        created_task = data["data"]["createTask"]
        assert created_task["title"] == "Test Task"
        assert created_task["description"] == "Test Description"
