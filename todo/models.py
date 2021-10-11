from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):

    email = models.EmailField(blank=False, max_length=254, verbose_name="email address")

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"

class TodoList(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True) 
    user = models.ForeignKey(CustomUser, related_name='todo', on_delete=models.CASCADE)
    def __str__(self):
        return self.title
