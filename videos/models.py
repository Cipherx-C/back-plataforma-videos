from django.db import models
from django.contrib.auth.models import AbstractUser
from nbformat import ValidationError

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def clean(self):
        if not self.url.startswith('http'):
            raise ValidationError('URL must start with "http"')

    def __str__(self):
        return self.title
