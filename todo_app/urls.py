from django.urls import path
from todo_app.views import (TodoTaskCreate,
                            TodoTaskUpdate,
                            TodoTaskDelete,
                            TodoTasksList,
                            change_task_status,
                            TagsList,
                            TagCreate,
                            TagUpdate,
                            TagDelete)

urlpatterns = [
    path("", TodoTasksList.as_view(), name="index"),
    path("task/create/", TodoTaskCreate.as_view(), name="task-create"),
    path("task/<int:pk>/update/", TodoTaskUpdate.as_view(), name="task-update"),
    path("task/<int:pk>/delete/", TodoTaskDelete.as_view(), name="task-delete"),
    path("task/<int:pk>/change_status/", change_task_status, name="task-change-status"),
    path("tags/", TagsList.as_view(), name="tag-list"),
    path("tag/create/", TagCreate.as_view(), name="tag-create"),
    path("tag/<int:pk>/update", TagUpdate.as_view(), name="tag-update"),
    path("tag/<int:pk>/delete", TagDelete.as_view(), name="tag-delete")
]
