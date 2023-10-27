from telnetlib import LOGOUT
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from carritos.models import *

# Create your views here.

def index(request):
    carritos= Carro.objects.all()

    return render(request, "index.html",{"carros": carritos})
    
def home(request):
    return render(request, 'home.html')
def vista(request):
    carritos= Carro.objects.all()

    return render(request, "index_admin.html",{"carros": carritos})

def buscar(request):
    serial = request.POST['texto_b']

def historico(request, codigo):
    serial =Historico.serial
    historico = Historico.objects.filter(serial=codigo)
    return render(request,"historico.html",{"historico":historico})
    

def sigin(request):
    if request.method == 'GET':
        return render(request, "login.html")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/index')
        else:
            error = "Usuario incorrecto"
            return render(request, 'login.html', {'error':error})
    else:
        return render(request, "login.html")
def notebook(request):
    notebook= Notebook.objects.all()
    return render(request,'notebook.html',{'note':notebook})


def contenido(request, codigo):
    serial =Carro.serial
    contenido = Notebook.objects.filter(Carro=codigo)
    return render(request,"notebook.html",{"con":contenido})

def sigout(request):
    logout(request)
    return render(request,'index.html')
