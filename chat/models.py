from __future__ import unicode_literals

from django.db import models
from usuarios.models import CustomUser
# Create your models here.

#clase que almacena la conversacion
class Conversacion(models.Model):
    emisor = models.ForeignKey(CustomUser,related_name='emisor') 
    receptor = models.ForeignKey(CustomUser,related_name='receptor')
    def __str__(self):
        return str(self.id)
    
    
class Mensaje(models.Model):
    texto = models.CharField(max_length=1000)
    conversacion = models.ForeignKey(Conversacion)
    usuario = models.ForeignKey(CustomUser)
    fichero = models.FileField(upload_to = 'static/documents',blank=True,null=True)
    #anadimos ficheros a los mensajes
    