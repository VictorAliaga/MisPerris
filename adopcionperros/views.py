from django.shortcuts import render

# Crea tus vistas aqui.

def index(request):
    return render(request, 'adopcionperros/index.html', {})

