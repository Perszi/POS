from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class Tag(models.Model):
    title = models.CharField(max_length=225)
    priority = models.IntegerField()

    def __str__(self):
        return self.title


class Movie(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    flyer = models.ImageField(upload_to='flyers', blank=True, null=True)
    file = models.FileField(upload_to='movies')
    tags = models.ManyToManyField(Tag)
    views = models.IntegerField()

    def __str__(self):
        return self.title





