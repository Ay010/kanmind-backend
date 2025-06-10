from django.db import models
from user_auth.models import User
from boards.models import Board
# Create your models here.


class Task(models.Model):
    board = models.ForeignKey(
        Board, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=255)
    priority = models.CharField(max_length=255)
    assignee = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='assigned_tasks', null=True, blank=True)
    reviewer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviewed_tasks')
    due_date = models.DateField()
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='created_tasks', null=True, blank=True)


class TaskComment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='task_comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name='comments')
