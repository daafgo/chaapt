from django.shortcuts import render,redirect
from django.db.models import Q
from django.contrib.auth.models import User
from .forms import *
from .models import *
# Vista encargada de gestionar la visualizacion del home dee la app
def home(request):
    users = User.objects.all()
    return render(request,"index.html", {'users':users})
 
 
#Vista encargada de gestionar la visualizacion de las conversaciones abiertas con los distintos usuarios de la aplicacion.        
def userchats(request,user_id):
    usuario = User.objects.get(id=user_id)
    #filtramos todos los chats en los que aparece el usuario como emisor o receptor
    chats = Conversacion.objects.filter(Q(receptor=user_id) | Q(emisor=user_id))
    #cogemos la coleccion de usuarios del sistema
    users = User.objects.exclude(id = user_id)
    #creamos una lista de los usuarios que tiene algun chat abierto con el usuario y otra con los usuarios con los que no hemos intecambiado ningun mensaje
    uchats={}
    nchats=[]
    for chat in chats:
        if chat.emisor==usuario:
            uchats[chat.receptor.username]=chat.id
        elif chat.receptor==usuario:
            uchats[chat.emisor.username]=chat.id
    #comparamos esta diccionario con la lista de usuarios de la aplicacion y obtenemos aquelllos con los que todavia no hemos iniciado una conversacion. 
    for u in users:
        if u.username not in uchats:
            nchats.append(u)
    return render(request,"chats.html",{'usuario':usuario,'chats':uchats,'nchats':nchats})

#Vista encargada de gestionar la visualizacion de las conversaciones    
def chatv(request,user_id,chat_id):
    conver= Conversacion.objects.get(id=chat_id) 
    #usuario que va enviar los mensajes
    user =  User.objects.get(id=user_id)
    if request.method=='POST':
        form = MensajeForm(request.POST)
        # Comprobamos que sea correcto:
        if form.is_valid():
           #añadimos el mensaje a la conversación
            nuevo_mensaje=Mensaje.objects.create(
               texto=form.cleaned_data['texto'],
               conversacion=conver,
               usuario=user
               )
            nuevo_mensaje.save()
    
    #usuario que los recibe
    
    if user==conver.receptor:
        usurec=conver.emisor
    else:
        usurec=conver.receptor
    mensajes = Mensaje.objects.filter(conversacion=conver)
    form=MensajeForm()
    return render(request,"conver.html",{'usurec':usurec,'msgs':mensajes,'user':user,'form':form})
    
    #vista que crea la conversacion y nos redirige a ella
def newchat(request,user_id,rec_id):
    
    emi=User.objects.get(id=user_id)
    rec=User.objects.get(id=rec_id)
    nueva_conver = Conversacion.objects.create(
        emisor=emi,
        receptor=rec
        )
    nueva_conver.save()
    
    return redirect('/'+user_id+'/'+str(nueva_conver.id)  )