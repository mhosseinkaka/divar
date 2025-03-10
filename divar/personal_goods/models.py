from django.db import models

# Create your models here.
select_gender = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )

class Shoes(models.Model):
    brand = models.CharField(max_length=50)
    size = models.IntegerField()
    price = models.IntegerField()
    types = models.CharField(max_length=20, choices=select_gender)

class Clothe(models.Model):
    brand = models.CharField(max_length=50)
    size = models.IntegerField()
    price = models.IntegerField()
    gen = models.CharField(max_length=20, choices=select_gender)

class Detail(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    product_owner = models.CharField(max_length=100)
    description = models.TextField()

    