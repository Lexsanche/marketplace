'''Back CRUD Usuarios'''
from django.db import models

# Create your models here.
class User(models.Model):
    '''Clase Usuarios'''
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.TextField()
    password = models.CharField(max_length=200)
    shippingAddress = models.CharField(max_length=200)
    cart = models.JSONField(blank=True, null=True)
    reviews = models.JSONField(blank=True, null=True)
