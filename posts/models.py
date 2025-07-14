from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Director(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.nombre

class Genero(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Pelicula(models.Model):
    titulo = models.CharField(max_length=200)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete=models.SET_NULL, null=True)
    año = models.PositiveIntegerField()

    def __str__(self):
        return self.titulo

class Review(models.Model):
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    imagen = models.ImageField(upload_to='reviews/', blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review de {self.pelicula} por {self.autor}"
