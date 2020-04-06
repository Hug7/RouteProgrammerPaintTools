from django.db import models

# Create your models here.
class Question(models.Model):
    id = models.CharField(max_length=10)