from django.db import models
from django.contrib.auth.models import User
from posts.models import Pelicula

class Review(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    texto = models.TextField()
    imagen = models.ImageField(upload_to='reviews/', null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reseña de {self.pelicula} por {self.autor}"

