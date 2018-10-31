from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Mascotas, AdoptarMascota
from .forms import ContactForm, LoginForm, RegisterForm
from django.contrib.auth.models import User

from django.contrib.auth import login,logout,authenticate # Importamos funciones de login logout y authenticate
from django.http import HttpResponseRedirect 

# Crea tus vistas aqui.

# Vista Principal Index.html

def index(request):
    mascotapublicada = Mascotas.objects.filter(FechaPublicado__lte=timezone.now()).order_by('FechaPublicado')
    return render(request, 'adopcionperros/index.html', {'mascotapublicada': mascotapublicada})    

# Vista de registro /registro/ donde va el formulario de registro de usuario

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

# Vista de log in /login/ donde va el formulario de log in de usuario

def login_view(request):
    mensaje =""
    if request.user.is_authenticated:
            return HttpResponseRedirect('/')
    else:
            if request.method == "POST":
                    form = LoginForm(request.POST)
                    if form.is_valid():
                            username = form.cleaned_data['username']
                            password = form.cleaned_data['password']
                            usuario = authenticate(username=username,password=password)
                            if usuario is not None and usuario.is_active:
                                    login(request,usuario)
                                    return HttpResponseRedirect('/')
                            else:
                                    mensaje = "Usuario y/o Password Incorrecto"
            form = LoginForm()
            ctx = {'form':form,'mensaje':mensaje}
            return render(request,'adopcionperros/login.html',ctx)

# Vista de logout /logout/ donde va el formulario de logout de usuario

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def adopcion_completa_view(request):
    return render(request, 'adopcionperros/adopcion_completa.html')

# Vista de la lista de mascotas /mascotas/ donde estan todas las mascotas de la pagina

def mascotas_view(request):
    masco = Mascotas.objects.filter(Estado="Disponible")
    ctx = {'mascota': masco}
    return render(request,'adopcionperros/mascotas.html',ctx)

# Vista en detalle de mascotas /perrito/ 
   
def perrito_detalle_view(request, pk):
    perris = get_object_or_404(Mascotas, pk=pk) 

    if (request.method == "POST"):
        Adoptador = request.user
        AdoptarMascota.objects.create(Adoptador=Adoptador, MascotaAdoptada=perris.NombreMascota)
        perris.update()

        return render(request, 'adopcionperros/adopcion_completa.html')

    else:
        ctx = {'mascotas':perris}
        return render(request,'adopcionperros/perrito_detalle.html',ctx)
