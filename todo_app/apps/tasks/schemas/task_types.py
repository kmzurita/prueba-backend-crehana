from strawberry import auto
from strawberry.django import type
from ..models.task import Task


@type(Task)
class TaskType:
    id: auto
    title: auto
    description: auto
    completed: auto
    created_at: auto
    updated_at: auto
