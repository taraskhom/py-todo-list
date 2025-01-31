from django.test import TestCase
from django.urls import reverse
from todo_app.models import TaskModel


class TaskStatusChangeTest(TestCase):

    def setUp(self):
        self.task = TaskModel.objects.create(content="Test Task", is_done=False)

    def test_change_task_status(self):
        self.assertFalse(self.task.is_done)

        response = self.client.get(reverse('task-change-status', args=[self.task.pk]))

        self.task.refresh_from_db()
        self.assertTrue(self.task.is_done)

        self.assertRedirects(response, reverse('index'))

    def test_change_task_status_not_found(self):
        response = self.client.get(reverse('task-change-status', args=[999]))
        self.assertEqual(response.status_code, 404)
