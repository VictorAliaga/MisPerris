from django.shortcuts import render
from django.utils import timezone
from .models import Mascotas

# Crea tus vistas aqui.

def index(request):
    mascotapublicada = Mascotas.objects.filter(FechaPublicado__lte=timezone.now()).order_by('FechaPublicado')
    return render(request, 'adopcionperros/index.html', {'mascotapublicada': mascotapublicada})







