from django.db import models
from django.utils import timezone

# Clase Adoptadores

class Adoptador(models.Model):
    NombreUsuario = models.Charfield(max_length=20, required= True, primary_key=True)
    ApellidoPaterno = models.Charfield(max_length=15, required= True)
    ApellidoMaterno = models.Charfield(max_length=15, required= True)
    NombreCompleto = models.Charfield(max_length=30, required= True)
    Correo = models.Emailfield(max_length=50, required= True)
    Contraseña = models.Charfield(max_length=15, required= True)
    ConfirmarContraseña = models.Charfield(max_length=15, required= True)

    # Metodo para Confirmar la Contraseña con la Confirmar Contraseña para crear el Usuario Adoptador
    def confirmar_usuario(self):
        self.Contraseña = self.ConfirmarContraseña
        self.save()

    # Retornamos el nombre del Usuario
    def __str__(self):
        return self.NombreUsuario

# Clase Mascotas

class Mascotas(models.Model):
    Imagen = models.ImageField(upload_to='templates/adopcionperros/perrisimagenes/')
    NombreMascota = models.Charfield(max_length=20, required= True, primary_key=True)
    RazaPredominante = models.Charfield(max_length=15, required= True)
    Descripcion = models.TextField(required= True)
    Estado = models.Charfield(max_length=30, required= True)




