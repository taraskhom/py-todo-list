from django.db import models


class TagModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class TaskModel(models.Model):
    content = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(TagModel, related_name="tasks")
