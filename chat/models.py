from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#clase que almacena la conversacion
class Conversacion(models.Model):
    emisor = models.ForeignKey(User,related_name='emisor') 
    receptor = models.ForeignKey(User,related_name='receptor')
    
    
    
class Mensaje(models.Model):
    texto = models.CharField(max_length=1000)
    conversacion = models.ForeignKey(Conversacion)

    