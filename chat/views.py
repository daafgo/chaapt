from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.models import User
from .models import *
# Create your views here.
def home(request):
    users = User.objects.all()
    return render(request,"index.html", {'users':users})
    
def userchats(request,user_id):
    usuario = User.objects.get(id=user_id)
    #filtramos todos los chats en los que aparece el usuario como emisor o receptor
    chats = Conversacion.objects.filter(Q(receptor=user_id) | Q(emisor=user_id))
    #cogemos la coleccion de usuarios del sistema
    users = User.objects.exclude(id = user_id)
    #creamos una lista de los usuarios que tiene algun chat abierto con el usuario
    uchats=[]
    nchats=[]
    for chat in chats:
        if chat.emisor==usuario:
            uchats.append(chat.receptor)
        elif chat.receptor==usuario:
            uchats.append(chat.emisor)
    print(uchats)
    for u in users:
        if u not in uchats:
            nchats.append(u)
    return render(request,"chats.html",{'chats':uchats,'nchats':nchats})
    
def chatv(request,user_id,chat_id):
    
    return render(request,"index.html")