from django.db import models
import uuid
# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, blank=True)
    # incomplete class right now. Need to implement functions for
    # updating, deleting, completing
    completed = models.BooleanField(default=False)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    userOwner = models.ForeignKey(User, on_delete=models.CASCADE)

