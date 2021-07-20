from django.db import models

# Create your models here.

class ToDoList(models.Model):
    id = models.IntegerField(default=0,primary_key=True)
    task = models.CharField(max_length=200)
