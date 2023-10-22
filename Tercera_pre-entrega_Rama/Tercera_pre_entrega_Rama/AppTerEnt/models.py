from django.db import models

# Create your models here.

class Destinos (models.Model):
        city = models.CharField(max_length=20)
        country =  models.CharField(max_length=20)
        category = models.CharField(max_length=20)
        popularity = models.IntegerField()

class Actividades (models.Model):
        name = models.CharField(max_length=30)
        difficulty =  models.CharField(max_length=30)
        duration = models.IntegerField()     

class Alojamientos (models.Model):
        name = models.CharField(max_length=30)
        city =  models.CharField(max_length=20)
        country =  models.CharField(max_length=20)
        adress =  models.CharField(max_length=20)
        stars = models.IntegerField()

class Atracciones (models.Model):
        name = models.CharField(max_length=30)
        city =  models.CharField(max_length=20)
        category =  models.CharField(max_length=20)
