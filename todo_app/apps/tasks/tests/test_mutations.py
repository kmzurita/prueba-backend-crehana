import pytest
from django.test import Client

@pytest.mark.django_db
class TestTaskMutations:
    def setup_method(self):
        self.client = Client()

    def test_create_task(self):
        pass
