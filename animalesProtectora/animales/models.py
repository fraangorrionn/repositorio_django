from django.conf import settings
from django.db import models
from django.utils import timezone


class Animal(models.Model):
    nombre = models.CharField(max_length=200)
    tipo = models.CharField(max_length=200)
    cuidador = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='animales'
    )

    def __str__(self):
        return self.nombre
    
class Protectora(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre
    
class Colaborador(models.Model):
    nombre = models.CharField(max_length=200)
    cargo = models.CharField(max_length=200)
    fecha_entrada_protectora = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre

