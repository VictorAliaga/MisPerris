from django.db import models
from django.utils import timezone

# Clase Adoptadores

class Adoptador(models.Model):
    NombreUsuario = models.CharField(max_length=20, primary_key=True)
    ApellidoPaterno = models.CharField(max_length=15)
    ApellidoMaterno = models.CharField(max_length=15)
    NombreCompleto = models.CharField(max_length=30)
    Correo = models.EmailField(max_length=50)
    Contraseña = models.CharField(max_length=15)
    ConfirmarContraseña = models.CharField(max_length=15)
    FechaRegistro = models.DateTimeField( default = timezone.now )

    # Metodo para Confirmar la Contraseña con la Confirmar Contraseña para crear el Usuario Adoptador
    def confirmar_usuario(self):
        self.Contraseña = self.ConfirmarContraseña
        self.save()

    # Retornamos el nombre del Usuario
    def __str__(self):
        return self.NombreUsuario

# Clase Mascotas

class Mascotas(models.Model):
    Imagen = models.ImageField(upload_to='adopcionperros/static/upload')
    NombreMascota = models.CharField(max_length=20,primary_key=True)
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

# Clase Formulario Adopcion Relacion Adoptador con Mascotas

class AdopcionMascota(models.Model):
    Adoptador = models.ForeignKey(Adoptador, null=False, blank=False, on_delete=models.CASCADE)
    Mascotas = models.ForeignKey(Mascotas, null=False, blank=False, on_delete=models.CASCADE)

    # Retornamos el Nombre de Usuario del Adoptador con la Mascota Adoptada
    def __str__(self):
        cadena = "{0} Ha Adoptado a {1}"
        return cadena.format(self.Adoptador.NombreUsuario, self.Mascotas.NombreMascota)




