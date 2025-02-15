from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Task(models.Model):

   user = models.ForeignKey(User, on_delete=models.CASCADE)
   title = models.CharField(max_length=100)
   description = models.TextField(blank=True)
   created_at = models.DateTimeField(default=timezone.now)

 


def __str__(self):
   return self.title

