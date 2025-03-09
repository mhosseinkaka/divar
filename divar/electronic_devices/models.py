from django.db import models

class E_device(models.Model):
    name = models.CharField(max_length=50)
    power = models.IntegerField()
    product_year = models.DateTimeField()
    price = models.IntegerField()

class Tablet(models.Model):
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    power = models.IntegerField()
    product_year = models.DateTimeField()
    price = models.IntegerField()
    ram = models.CharField(max_length=10)
    cpu = models.CharField(max_length=50)

class Mobile(models.Model):
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    power = models.IntegerField()
    product_year = models.DateTimeField()
    price = models.IntegerField()
    ram = models.CharField(max_length=10)
    cpu = models.CharField(max_length=50)

class Computers(models.Model):
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    power = models.IntegerField()
    product_year = models.DateTimeField()
    price = models.IntegerField()
    ram = models.CharField(max_length=10)
    cpu = models.CharField(max_length=50)
    hard = models.CharField(max_length=15)

class Game_console(models.Model):
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    power = models.IntegerField()
    product_year = models.DateTimeField()
    price = models.IntegerField()
    ram = models.CharField(max_length=10)
    cpu = models.CharField(max_length=50)
    model_divice = models.CharField(max_length=15)

class  Video_audio(models.Model):
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    power = models.IntegerField()
    product_year = models.DateTimeField()
    price = models.IntegerField()
    size = models.IntegerField()
    model_device = models.CharField(max_length=15)
    