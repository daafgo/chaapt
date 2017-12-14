from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.files.storage import FileSystemStorage


# extendemos la clase usuario 
class CustomUser(AbstractUser):
    estado = models.CharField(max_length=100)  #Alias de usuario
    photo = models.ImageField(upload_to='photos/',default='/static/img/default/defaultProfile.png', blank=True)
