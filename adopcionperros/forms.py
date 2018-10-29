from django import forms
from django.contrib.auth.models import User

class ContactForm(forms.Form):
    Email = forms.EmailField(widget=forms.TextInput())
    Titulo = forms.CharField(widget=forms.TextInput())
    Texto = forms.CharField(widget=forms.Textarea())

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput(render_value=False))

class RegisterForm(forms.Form):
    username = forms.CharField(label="Nombre de Usuario",widget=forms.TextInput())
    lastname = forms.CharField(label="Apellido Paterno",widget=forms.TextInput())
    firstname = forms.CharField(label="Nombre",widget=forms.TextInput())
    email = forms.EmailField(label="Correo Electronico",widget=forms.TextInput())
    password_one = forms.CharField(label="Contraseña",widget=forms.PasswordInput(render_value=False))
    password_two = forms.CharField(label="Confirmar Contraseña",widget=forms.PasswordInput(render_value=False))

    # Validamos que el Nombre de Usuario sea Unico e Irrepetible
    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            u = User.objects.get(username=username)
        except User.DoesNotExist:
            return username        
        raise forms.ValidationError('ERROR: Este nombre de usuario ya existe!')

    # Validamos que el Correo sea Unico e Irrepetible
    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            u = User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('ERROR: Este Email ya esta Registrado!')

    # Validamos la contraseña 2
    def clean_password_two(self):
        password_one = self.cleaned_data['password_one']
        password_two = self.cleaned_data['password_two']
        if password_one == password_two:
            pass
        else:
            raise forms.ValidationError('ERROR: Las Contraseñas no coinciden!')