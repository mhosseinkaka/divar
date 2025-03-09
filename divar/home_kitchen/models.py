from django.db import models

# Create your models here.
class Home_object(models.Model):
    name = models.CharField(max_length=100)
    year = models.DateTimeField()
    weight = models.IntegerField()
    price = models.IntegerField()
    creator = models.CharField(max_length=100)
    place = models.TextField()