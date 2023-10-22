from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Formulario(forms.Form):

        Destino_Ciudad = forms.CharField(max_length=20)
        Destino_Pais =  forms.CharField(max_length=20)
        Destino_Categoria = forms.CharField(max_length=20)
        Destino_Popularidad = forms.IntegerField()

class Formact(forms.Form):
        Actividad_Nombre = forms.CharField(max_length=30)
        Actividad_Dificultad =  forms.CharField(max_length=30)
        Actividad_Duracion = forms.IntegerField()

class Formal(forms.Form):     
        Alojamiento_Nombre = forms.CharField(max_length=30)
        Alojamiento_Ciudad =  forms.CharField(max_length=20)
        Alojamiento_Pais =  forms.CharField(max_length=20)
        Alojamiento_Direccion =  forms.CharField(max_length=20)
        Alojamiento_Estrellas = forms.IntegerField()

class Formatr(forms.Form):
        Atraccion_Nombre = forms.CharField(max_length=30)
        Atraccion_Ciudad =  forms.CharField(max_length=20)
        Atraccion_Categoria =  forms.CharField(max_length=20)


class Buscar(forms.Form):
        Destino_Ciudad = forms.CharField(max_length=20)

class UserRegisterForm(UserCreationForm):
        username = forms.CharField (label = "Usuario")
        first_name = forms.CharField (label = "Nombre")
        last_name = forms.CharField (label = "Apellido")
        email = forms.EmailField()
        password1 = forms.CharField (label = "Contraseña", widget = forms.PasswordInput)
        password2 = forms.CharField (label = "Repetir contraseña", widget = forms.PasswordInput)

        class Meta:
                model= User
                fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

                help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):

        first_name = forms.CharField (label = "Nombre")
        last_name = forms.CharField (label = "Apellido")
        email = forms.EmailField()
        password1 = forms.CharField (label = "Contraseña", widget = forms.PasswordInput)
        password2 = forms.CharField (label = "Repetir contraseña", widget = forms.PasswordInput) 

        class Meta:
                model= User
                fields = ['first_name', 'last_name', 'email', 'password1', 'password2']

                help_texts = {k:"" for k in fields}

        