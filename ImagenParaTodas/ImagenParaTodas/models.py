from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class Tip(models.Model):
    descripcion=models.CharField(max_length=500)

class Cuerpo(models.Model):
    descripcion= models.CharField(max_length=500)
    tipo= models.CharField(max_length=30)
    
class Vestido(models.Model):
    nombre= models.CharField(max_length=30)
    descripcion= models.CharField(max_length=500)
    color= models.CharField(max_length=100)