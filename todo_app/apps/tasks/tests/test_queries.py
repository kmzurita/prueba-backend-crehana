import pytest
from django.test import Client


@pytest.mark.django_db
class TestTaskQueries:
    def setup_method(self):
        self.client = Client()

    def test_get_tasks(self):
        pass