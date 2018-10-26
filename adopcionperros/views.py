from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import render
from django.utils import timezone
from .models import Mascotas
from .forms import ContactForm, LoginForm, RegisterForm
from django.contrib.auth.models import User

from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect

# Crea tus vistas aqui.

# Vista Principal Index.html
def index(request):
    mascotapublicada = Mascotas.objects.filter(FechaPublicado__lte=timezone.now()).order_by('FechaPublicado')
    return render(request, 'adopcionperros/index.html', {'mascotapublicada': mascotapublicada})

# Vista de registro /registro/ donde va el formulario de registro de usuario
# Nota: se adapto el codigo a la version actual de django
def register_view(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['username']
            lastname = form.cleaned_data['lastname']
            firstname = form.cleaned_data['firstname']
            email = form.cleaned_data['email']
            password_one = form.cleaned_data['password_one']
            password_two = form.cleaned_data['password_two']
            u = User.objects.create_user(username=usuario,last_name=lastname,first_name=firstname,email=email,password=password_one)
            # Registramos el Usuario
            u.save()
            # Redireccionamos a la pagina de confirmacion de registro exitoso
            return render(request,'adopcionperros/registro_exitoso.html')
        else:
            ctx = {'form':form}
            return render(request,'adopcionperros/registro.html',ctx)
    ctx = {'form':form}
    return render(request,'adopcionperros/registro.html',ctx)    









