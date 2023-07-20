from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User






# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=80)
    username = models.CharField(max_length=80,primary_key=True)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    confirmpassword = models.CharField(max_length=40)
    status = models.CharField(max_length=10, default='U')

    def __str__(self):
        return self.username

class Post(models.Model):
    thumbnail = models.ImageField(max_length=80)
    title = models.CharField(max_length=80)
    desc = models.TextField()
    username = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
