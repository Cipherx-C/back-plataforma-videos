from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='videos_users',
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        verbose_name=('groups')
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='videos_users',
        blank=True,
        help_text=('Specific permissions for this user.'),
        verbose_name=('user permissions')
    )

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

    def __str__(self):
        return self.title