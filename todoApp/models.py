from django.db import models
from django.db.models.fields import CharField, DateTimeField

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
