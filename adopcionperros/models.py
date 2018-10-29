from django.db import models
from django import forms
from django.utils import timezone

# Clase Mascotas
class Mascotas(models.Model):
    Imagen = models.ImageField(upload_to='upload')
    NombreMascota = models.CharField(max_length=20)
    RazaPredominante = models.CharField(max_length=15)
    Descripcion = models.TextField()
    Estado = (('R','Rescatado'), ('D','Disponible'), ('A','Adoptado'))
    ESTADO = models.CharField(max_length=1, choices=Estado, default='R')
    FechaPublicado = models.DateTimeField(blank=True, null=True)

    # Retornamos el nombre de la mascota
    def __str__(self):
        return self.NombreMascota

    # Comprobamos que la fecha de publicado sea la actual
    def mascota_publicada(self):
        self.FechaPublicado = timezone.now()
        self.save()