from django.db import models

# Create your models here.
class Marca(models.Model):
    nombre = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nombre


class Ubicacion(models.Model):
    lugar = models.CharField(max_length=12)
    piso = models.CharField(max_length=12)

    def __str__(self):
        return self.lugar

class Carro(models.Model):
    serial= models.CharField(primary_key=True,max_length=20)
    activo_fijo= models.CharField(max_length=20)
    año_entrada=models.CharField(max_length=4)
    año_baja=models.CharField(max_length=4, null=True)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)
    estado = models.CharField(max_length=6)
    def __str__(self):
        return self.serial

class Notebook(models.Model):
    serial= models.CharField(primary_key=True,max_length=20)
    activo_fijo= models.CharField(max_length=20)
    modelo = models.CharField(max_length=30)
    marca=models.ForeignKey(Marca, on_delete=models.CASCADE)
    carro= models.ForeignKey(Carro, on_delete=models.CASCADE)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE, null=True)
    imagen = models.ImageField(upload_to = 'act_notebook', null=True) 
    def __str__(self):
        return self.serial

class PC(models.Model):
    serial= models.CharField(primary_key=True,max_length=20)
    activo_fijo= models.CharField(max_length=20)
    modelo = models.CharField(max_length=30)
    marca=models.ForeignKey(Marca, on_delete=models.CASCADE)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE, null=True)
    imagen = models.ImageField(upload_to = 'act_pc', null=True)
    def __str__(self):
        return self.serial
    
class Historico (models.Model):
    serial = models.CharField(max_length=20)
    activo_fijo= models.CharField(max_length=20)
    fecha = models.DateField()
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)
    def __str__(self):
        return self.serial

class Usuario (models.Model):
    user = models.CharField(max_length=20)
    passwrd = models.CharField(max_length=12)
    def __str__(self):
        return self.user

class Proyector(models.Model):
    serial= models.CharField(primary_key=True, max_length=20)
    activo_fijo= models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)
    marca=models.ForeignKey(Marca, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to = 'act_proyector', null=True)
    def __str__(self):
        return self.serial