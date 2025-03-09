from django.db import models

# Create your models here.
class Entertainment(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='entertainment_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Ticket(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    place = models.CharField(max_length=20)

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    place = models.CharField(max_length=20)

class Tour(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    place = models.CharField(max_length=20)
    start = models.CharField(max_length=200)
    city_name = models.CharField(max_length=200)

class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.CharField(max_length=20)

class Scoter(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    size = models.IntegerField()
    model_device = models.CharField(max_length=100)

