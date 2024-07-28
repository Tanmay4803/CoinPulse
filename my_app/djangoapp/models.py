from django.db import models

# Create your models here.
class Alert(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    current = models.CharField(max_length=50)
    target = models.CharField(max_length=50)
