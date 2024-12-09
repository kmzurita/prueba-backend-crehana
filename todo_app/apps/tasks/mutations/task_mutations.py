import strawberry
from typing import Optional
from ..schemas.task_schema import TaskType
from ..models.task import Task


@strawberry.type
class TaskMutations:
    @strawberry.mutation
    def create_task(
        self, title: str, description: str = "", completed: bool = False
    ) -> TaskType:
        task = Task.objects.create(
            title=title, description=description, completed=completed
        )
        return task

    @strawberry.mutation
    def update_task(
        self,
        id: int,
        title: Optional[str] = None,
        description: Optional[str] = None,
        completed: Optional[bool] = None,
    ) -> TaskType:
        task = Task.objects.get(pk=id)
        if title is not None:
            task.title = title
        if description is not None:
            task.description = description
        if completed is not None:
            task.completed = completed
        task.save()
        return task

    @strawberry.mutation
    def delete_task(self, id: int) -> bool:
        try:
            Task.objects.get(pk=id).delete()
            return True
        except Task.DoesNotExist:
            return False
