from django.contrib.auth import authenticate
from django.shortcuts import redirect, render

from carritos.models import *

# Create your views here.
def home(request):
    carritos= Carro.objects.all()

    return render(request, "index.html",{"carros": carritos})
def vista(request):
    carritos= Carro.objects.all()

    return render(request, "index_admin.html",{"carros": carritos})

def buscar(request):
    serial = request.POST['texto_b']

def historico(request, codigo):
    serial =Historico.serial
    historico = Historico.objects.filter(serial=codigo)
    return render(request,"historico.html",{"historico":historico})
    
def login(request):
    return render(request, "login.html")
def autenticate(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if Usuario.objects.filter(user=username).exists():
            user = Usuario.objects.get(user=username)
            if user.passwrd== password:
                return redirect('/vista')
            else:
                return redirect('/login')
        else:
            return redirect('/login')
    else:
        return render(request, 'login.html')
