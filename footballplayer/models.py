from django.db import models

# Create your models here.

class FootballPlayer(models.Model):
    name = models.CharField(max_length=50)
    team = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    age = models.IntegerField()
    shirt_number = models.CharField(max_length=2)
    position = models.CharField(max_length=2)
