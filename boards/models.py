from django.db import models
from user_auth.models import User


# Create your models here.


class Board(models.Model):
    title = models.CharField(max_length=255)
    members = models.ManyToManyField(User, related_name='boards')
    owner_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='owned_boards')
