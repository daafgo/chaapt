from django.shortcuts import render
from usuarios.models import CustomUser
# Create your views here.


#vista para controlar el perfil de un usuario
def profile(request,user_id):
    user = CustomUser.objects.get(id=user_id)
    return render(request,"profile.html", {'user':user})