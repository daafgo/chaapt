#!/usr/bin/python
# -*- coding: latin-1 -*-
from django.shortcuts import render,redirect
from django.db.models import Q
from django.contrib.auth.models import User
from usuarios.models import CustomUser
from .forms import *
from .models import *
from emoji import Emoji
# Vista encargada de gestionar la visualizacion del home dee la app
def home(request):
    users = CustomUser.objects.all()
    return render(request,"index.html", {'users':users})
 
 
#Vista encargada de gestionar la visualizacion de las conversaciones abiertas con los distintos usuarios de la aplicacion.        
def userchats(request,user_id):
    usuario = CustomUser.objects.get(id=user_id)
    #filtramos todos los chats en los que aparece el usuario como emisor o receptor
    chats = Conversacion.objects.filter(Q(receptor=user_id) | Q(emisor=user_id))
    #cogemos la coleccion de usuarios del sistema
    users = CustomUser.objects.exclude(id = user_id)
    #creamos una lista de los usuarios que tiene algun chat abierto con el usuario y otra con los usuarios con los que no hemos intecambiado ningun mensaje
    uchats={}
    nchats=[]
    for chat in chats:
        if chat.emisor==usuario:
            uchats[chat.receptor]=chat.id
        elif chat.receptor==usuario:
            uchats[chat.emisor]=chat.id
    #comparamos esta diccionario con la lista de usuarios de la aplicacion y obtenemos aquelllos con los que todavia no hemos iniciado una conversacion. 
    for u in users:
        if u not in uchats:
            nchats.append(u)
    return render(request,"chats.html",{'usuario':usuario,'chats':uchats,'nchats':nchats})

#Vista encargada de gestionar la visualizacion de las conversaciones    
def chatv(request,user_id,chat_id):
    conver= Conversacion.objects.get(id=chat_id) 
    #usuario que va enviar los mensajes
    User =  CustomUser.objects.get(id=user_id)
    if request.method=='POST':
        form = MensajeForm(request.POST, request.FILES)
        print(request.FILES)
        if request.FILES :
            if form.is_valid():
               #añadimos el mensaje a la conversación
                   
                nuevo_mensaje=Mensaje.objects.create(
                   texto=form.cleaned_data['texto'],
                   conversacion=conver,
                   usuario=User,
                   fichero = request.FILES['file']
                   )
                nuevo_mensaje.save()
        else:
        # Comprobamos que sea correcto:
            if form.is_valid():
               #añadimos el mensaje a la conversación
                nuevo_mensaje=Mensaje.objects.create(
                   texto=form.cleaned_data['texto'],
                   conversacion=conver,
                   usuario=User
                  # fichero = request.FILES['file']
                   )
                nuevo_mensaje.save()
        # print (form.errors)
    #usuario que los recibe
    
    if User==conver.receptor:
        usurec=conver.emisor
    else:
        usurec=conver.receptor
    mensajes = Mensaje.objects.filter(conversacion=conver)
    form=MensajeForm()
    #cargamos la lista de emojis le ponemos un limite para que no tarde mucho
    emojis=[]
    for i, emoji in enumerate(sorted(Emoji.keys())):
        if i >= 1000:
            break
        emojis.append(':{0}:'.format(emoji))


    
    return render(request,"conver.html",{'emojis':emojis,'usuario':User,'usurec':usurec,'msgs':mensajes,'CustomUser':CustomUser,'form':form})
    
    #vista que crea la conversacion y nos redirige a ella
def newchat(request,user_id,rec_id):
    
    emi=CustomUser.objects.get(id=user_id)
    rec=CustomUser.objects.get(id=rec_id)
    nueva_conver = Conversacion.objects.create(
        emisor=emi,
        receptor=rec
        )
    nueva_conver.save()
    
    return redirect('/'+user_id+'/'+str(nueva_conver.id))