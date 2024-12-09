import strawberry
from typing import List
from .task_types import TaskType
from ..models import Task
from ..mutations import TaskMutations


@strawberry.type
class Query:
    @strawberry.field
    def tasks(self) -> List[TaskType]:
        return Task.objects.all()

    @strawberry.field
    def task(self, id: int) -> TaskType:
        return Task.objects.get(pk=id)


schema = strawberry.Schema(query=Query, mutation=TaskMutations)
