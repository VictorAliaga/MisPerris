from django import forms


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


