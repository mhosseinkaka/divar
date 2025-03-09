from django.db import models

# Create your models here.
class Job_detail(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    salary = models.IntegerField()
    place = models.CharField(max_length=100)
    history = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)