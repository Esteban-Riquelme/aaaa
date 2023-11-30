from .models import *
from telnetlib import LOGOUT
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Permission, User, Group
from django.shortcuts import redirect, render



# Create your views here.

def carros(request):
    carritos= Carro.objects.all()

    return render(request, "carros.html",{"carros": carritos})
    
def home(request):
    return render(request, 'home.html')
def vista(request):
    carritos= Carro.objects.all()

    return render(request, "index_admin.html",{"carros": carritos})

def buscar(request):
    serial = request.POST['texto_b']

def historico(request, codigo):
    if request.method == 'GET':
        serial =Historico.serial
        historico = Historico.objects.filter(serial=codigo)
        image_name = f"image_{codigo}.png"

        # Aquí debes agregar la lógica para obtener la URL completa de la imagen
        image_url = f"{image_name}"
        return render(request,"historico.html",{"i":image_url,"historico":historico})
    elif request.method == 'POST':
        ubi = request.POST['ubi']
    

def sigin(request):
    logout(request)
    if request.method == 'GET':
        return render(request, "login.html")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
      
        if user is not None:
            login(request,user)
            return redirect('home')
            
        else:
            error = "Usuario incorrecto"
            return render(request, 'login.html', {'error':error})
    else:
        return render(request, "login.html")
def notebook(request):
    if request.method == 'GET':
        notebook= Notebook.objects.all()
        return render(request,'notebook.html',{'note':notebook})
    else:
        activo = username = request.POST['activo']
        notebook= Notebook.objects.get(serial=activo)
        return render(request,'notebook.html',{'ac':notebook})

def contenido(request, codigo):
    if request.method == 'GET':
        notebook = Notebook.objects.filter(carro = codigo)
        return render(request,"notebook.html",{"con":notebook})
    else:
        activo = username = request.POST['activo']
        notebook= Notebook.objects.get(serial=activo)
        return render(request,'notebook.html',{'ac':notebook})


def sigout(request):
    logout(request)
    return redirect('/')

def proyector(request):
    proyector= Proyector.objects.all()
    return render(request,"proyectores.html",{'pro':proyector})
