from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import uuid
# class User(models.Model):
#     name = models.CharField(max_length=50)
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4)


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, blank=True)
    completed = models.BooleanField(default=False)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    userOwner = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('accounts/profile/', args=[str(self.id)])