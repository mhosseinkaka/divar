from django.db import models

# Create your models here.

class Vehicle(models.Model):
    engine = models.IntegerField()
    cc = models.IntegerField()
    sokht = models.CharField(max_length=20)
    vazn = models.IntegerField()
    number_sarneshin = models.IntegerField()
    country_product = models.CharField(max_length=25)

class Car(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    detail = models.ForeignKey(to=Vehicle, on_delete=models.CASCADE)

class Truck(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    detail = models.ForeignKey(to=Vehicle, on_delete=models.CASCADE)

class Motor(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    detail = models.ForeignKey(to=Vehicle, on_delete=models.CASCADE)