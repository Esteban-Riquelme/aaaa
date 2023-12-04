from .models import *
from telnetlib import LOGOUT
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Permission, User, Group
from django.shortcuts import redirect, render
from django.utils import timezone



# inicio
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

def sigout(request):
    logout(request)
    return redirect('/')

def home(request):
    return render(request, 'home.html')


    

#funciones

def buscar(request):
    serial = request.POST['texto_b']

def historico(request, codigo):
    serial =Historico.serial
    historico = Historico.objects.filter(serial=codigo)
    if request.method == 'GET':
        
        return render(request,"historico.html",{"historico":historico})
    elif request.method == 'POST':
        if Historico.objects.filter(serial=codigo):
            his = Historico.objects.filter(serial=codigo)
            ubi = request.POST['ubi']
            ubi = Ubicacion.objects.get(lugar = ubi)
            try:    
                PC.objects.get(serial=codigo)
                pc = PC.objects.get(serial=codigo)
                pc.ubicacion = ubi
                now = timezone.now()
                pc.save()
                his = Historico.objects.create(serial = codigo, activo_fijo = pc.activo_fijo,fecha =now, ubicacion = ubi )
                return render(request,"historico.html",{"historico":historico})
            except PC.DoesNotExist:
                pass
            try:    
                Notebook.objects.get(serial=codigo)
                note = Notebook.objects.get(serial=codigo)
                note.ubicacion = ubi 
                now = timezone.now()
                note.save()
                his = Historico.objects.create(serial = codigo, activo_fijo = note.activo_fijo,fecha =now, ubicacion = ubi )
                return render(request,"historico.html",{"historico":historico})
            except Notebook.DoesNotExist:
                pass
        else:
            try:
                Notebook.objects.get(serial=codigo)
                ubi = request.POST['ubi']
                ubi = Ubicacion.objects.get(lugar = ubi)
                note = Notebook.objects.get(serial=codigo)
                note.ubicacion = ubi 
                now = timezone.now()
                note.save()
                his = Historico.objects.create(serial = codigo, activo_fijo = note.activo_fijo,fecha =now, ubicacion = ubi )
                return render(request,"historico.html",{"historico":historico})
            except Notebook.DoesNotExist:
                pass
            try:
                PC.objects.get(serial=codigo) 
                ubi = request.POST['ubi']
                ubi = Ubicacion.objects.get(lugar = ubi)
                pc = PC.objects.get(serial=codigo)
                pc.ubicacion = ubi
                now = timezone.now()
                pc.save()
                his = Historico.objects.create(serial = codigo, activo_fijo = pc.activo_fijo,fecha =now, ubicacion = ubi )
                return render(request,"historico.html",{"historico":historico})
            except PC.DoesNotExist:
                pass
            
  
#equipos

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

def pc(request):
    if request.method == 'GET':
        pc= PC.objects.all()
        return render(request,'pc.html',{'pc':pc})
    else:
        activo = username = request.POST['activo']
        notebook= Notebook.objects.get(serial=activo)
        return render(request,'notebook.html',{'ac':notebook})

def proyector(request):
    proyector= Proyector.objects.all()
    return render(request,"proyectores.html",{'pro':proyector})

def carros(request):
    carritos= Carro.objects.all()

    return render(request, "carros.html",{"carros": carritos})