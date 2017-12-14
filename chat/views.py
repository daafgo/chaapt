from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    users = User.objects.all()
    return render(request,"index.html", {'users':users})
    
def userchats(request,user_id):
    
    return render(request,"index.html")
    
def chatv(request,user_id,chat_id):
    
    return render(request,"index.html")