from django.db import models
from user.models import User

class Categoria(models.Model):
    id          = models.AutoField(primary_key=True)
    name        = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image       = models.ImageField(upload_to='media/Category', blank=True, null=True)
    def __str__(self):
        return self.name
class Item(models.Model):
    id          = models.AutoField(primary_key=True)
    sellerID    = models.IntegerField(blank=True,null=True)
    name        = models.CharField(max_length=255)
    category    = models.ForeignKey(Categoria,on_delete = models.CASCADE)
    description = models.TextField(blank=True, null=True)
    price       = models.FloatField()
    stock       = models.BooleanField()
    image       = models.ImageField(upload_to='media/Items', blank=True, null=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    questions = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    id          = models.AutoField(primary_key=True)
    item        = models.ForeignKey(Item,on_delete = models.CASCADE)
    score       = models.IntegerField()
    review      = models.CharField(max_length = 255)
    date        = models.DateField()
    image       = models.ImageField(upload_to='media/Items/Reviews', blank=True, null=True)
    def __str__(self):
        return self.id
class Status(models.Model):
    COMPRADO    = "Comprado"
    ENVIADO     = "Enviado"
    ENTREGADO   = "Entregado"
    STATUS_CHOICES =[(COMPRADO,"Comprado"),(ENVIADO,"Enviado"),(ENTREGADO,"Entregado")]
    status      = models.CharField(max_length=255,choices=STATUS_CHOICES,default=COMPRADO)

class Order(models.Model):
    id          = models.AutoField(primary_key=True)
    userID      = models.ForeignKey(User, on_delete = models.CASCADE)
    date        = models.DateField()
    status      = models.CharField(max_length = 255)
    total       = models.FloatField()
    cart        = models.JSONField()
    def __str__(self):
        return self.id