from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import get_object_or_404, redirect
from todo_app.forms import TaskForm

from todo_app.models import TaskModel, TagModel


class TodoTasksList(generic.ListView):
    model = TaskModel
    template_name = "todo/index.html"
    context_object_name = "tasks"
    ordering = ["is_done", "-created_at"]


def change_task_status(request, pk):
    task = get_object_or_404(TaskModel, pk=pk)
    task.is_done = not task.is_done
    task.save()
    return redirect("index")


class TodoTaskCreate(generic.CreateView):
    model = TaskModel
    template_name = "todo/task_form.html"
    form_class = TaskForm
    success_url = reverse_lazy("index")


class TodoTaskUpdate(generic.UpdateView):
    model = TaskModel
    template_name = "todo/task_form.html"
    form_class = TaskForm
    success_url = reverse_lazy("index")


class TodoTaskDelete(generic.DeleteView):
    model = TaskModel
    template_name = "todo/task_confirm_delete.html"
    success_url = reverse_lazy("index")


class TagsList(generic.ListView):
    model = TagModel
    template_name = "todo/tag_list.html"
    context_object_name = "tags"


class TagCreate(generic.CreateView):
    model = TagModel
    template_name = "todo/tag_form.html"
    fields = ["name"]
    success_url = reverse_lazy("tag-list")


class TagUpdate(generic.UpdateView):
    model = TagModel
    template_name = "todo/tag_form.html"
    fields = ["name"]
    success_url = reverse_lazy("tag-list")


class TagDelete(generic.DeleteView):
    model = TagModel
    template_name = "todo/tag_confirm_delete.html"
    success_url = reverse_lazy("tag-list")
