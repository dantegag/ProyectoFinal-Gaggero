from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    bio = models.TextField(blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Perfil

@receiver(post_save, sender=User)
def crear_o_actualizar_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)
    else:
        # Si ya existe, intentamos guardar el perfil asociado
        if hasattr(instance, 'perfil'):
            instance.perfil.save()

