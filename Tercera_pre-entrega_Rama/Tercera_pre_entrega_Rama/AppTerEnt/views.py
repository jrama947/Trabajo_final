from django.shortcuts import render
from .models import Destinos, Actividades, Alojamientos, Atracciones
from AppTerEnt.forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

def inicio(request):
    return render(request, "AppTerEnt/index.html")



def destinos(request):
    return render(request, "AppTerEnt/destinos.html")


def atracciones(request):
    return render(request, "AppTerEnt/atracciones.html")

def actividades(request):
    return render(request, "AppTerEnt/actividades.html")


def alojamientos(request):
    return render(request, "AppTerEnt/alojamientos.html")


def formulario(request):
 
      if request.method == "POST":
 
            miFormulario = Formulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  destino = Destinos(city = request.POST['Destino_Ciudad'], country = request.POST['Destino_Pais'], category = request.POST['Destino_Categoria'], popularity = request.POST['Destino_Popularidad'])
                  actividad = Actividades(name = request.POST['Actividad_Nombre'], difficulty = request.POST['Actividad_Dificultad'], duration = request.POST['Actividad_Duracion'])
                  alojamiento = Alojamientos(name = request.POST['Alojamiento_Nombre'], city = request.POST['Alojamiento_Ciudad'], country = request.POST['Alojamiento_Pais'], adress = request.POST['Alojamiento_Direccion'], stars = request.POST['Alojamiento_Estrellas'])
                  atraccion = Atracciones(name = request.POST['Atraccion_Nombre'], city = request.POST['Atraccion_Ciudad'], category = request.POST['Atraccion_Categoria'])
                  destino.save()
                  actividad.save()
                  alojamiento.save()
                  atraccion.save()

                  return render(request, "AppTerEnt/index.html")
      else:
            miFormulario = Formulario()
 
      return render(request, "AppTerEnt/formulario.html", {"miFormulario": miFormulario})


def buscar(request):
 
      if request.method == "POST":
 
            miFormulario = Buscar(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data

                  destinos = Destinos.objects.filter(city__icontains=informacion["Destino_Ciudad"])

                  return render(request, "AppTerEnt/lista.html", {"destinos": destinos})
      else:
            miFormulario = Buscar()
 
      return render(request, "AppTerEnt/mostrar.html", {"miFormulario": miFormulario})


def mostrar(request):
     pass

def about(request):
     return render(request, "AppTerEnt/about.html")


def nz(request):
     return render(request, "AppTerEnt/nz.html")


def ind(request):
     return render(request, "AppTerEnt/ind.html")


def jap(request):
     return render(request, "AppTerEnt/jap.html")


def mtcook(request):
     return render(request, "AppTerEnt/mtcook.html")


def arrocera(request):
     return render(request, "AppTerEnt/arrocera.html")


def bj(request):
     return render(request, "AppTerEnt/bj.html")


def buceo(request):
     return render(request, "AppTerEnt/buceo.html")

def sama(request):
     return render(request, "AppTerEnt/sama.html")


def welcome(request):
     return render(request, "AppTerEnt/welcome.html")

# Definición de funciones para login, registro y edición de usuarios.

def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "AppTerEnt/index.html", {"mensaje":f"Bienvenido {usuario}!"})
           
        else:
            form = AuthenticationForm(request)
            return render(request, "AppTerEnt/login.html", {"mensaje":"Datos incorrectos", "form": form})

    form = AuthenticationForm()

    return render(request, "AppTerEnt/login.html", {"form": form})

def register(request):

     if request.method == "POST":
          form = UserRegisterForm(request.POST)

          if form.is_valid():

               form.save()
               return render(request, "AppTerEnt/index.html", {"mensaje": "Te has registrado correctamente!"})

     else:
          form = UserRegisterForm()
          
     return render(request, "AppTerEnt/register.html", {"form": form})

def edit (request):
     usuario = request.user

     if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            if informacion["password1"] != informacion["password2"]:
                 datos = {
                      'first_name': usuario.first_name,
                      'last_name': usuario.last_name,
                      'email': usuario.email
                 }
                 miFormulario = UserEditForm(initial=datos)

            else:

                  usuario.first_name = informacion['first_name']
                  usuario.last_name = informacion['last_name']
                  usuario.email = informacion['email']
                  usuario.set_password(informacion["password1"])
                  #usuario.password1 = informacion['password2']

                  usuario.save()

                  return render(request, "AppTerEnt/index.html")


     miFormulario = UserEditForm(initial={'first_name': usuario.first_name, 'last_name': usuario.last_name, 'email': usuario.email})

     return render(request, "AppTerEnt/edituser.html", {"mi_form": miFormulario})

def es_administrador(user):
     return user.is_superuser
#Clases para visualizar diferentes tablas de la BD.

class DestinosListView(LoginRequiredMixin, ListView):
      
      model = Destinos
      template_name = "AppTerEnt/listdest.html"

class AtraccionesListView(LoginRequiredMixin,ListView):
      
      model = Atracciones
      template_name = "AppTerEnt/listatr.html"

class AlojamientosListView(LoginRequiredMixin,ListView):
      
      model = Alojamientos
      template_name = "AppTerEnt/listal.html"

class ActividadesListView(LoginRequiredMixin,ListView):
      
      model = Actividades
      template_name = "AppTerEnt/listact.html"

#Clases para visualizar detalles de diferentes tablas de la BD.

class DestinosDetalle(LoginRequiredMixin,DetailView):
      
      model = Destinos
      template_name = "AppTerEnt/detaildest.html"

class AtraccionesDetalle(LoginRequiredMixin,DetailView):
      
      model = Atracciones
      template_name = "AppTerEnt/detailatr.html"

class AlojamientosDetalle(LoginRequiredMixin,DetailView):
      
      model = Alojamientos
      template_name = "AppTerEnt/detailal.html"

class ActividadesDetalle(LoginRequiredMixin,DetailView):
      
      model = Actividades
      template_name = "AppTerEnt/detailact.html"

#Clases para crear registros en las diferentes tablas de la BD.

class DestinosCreateView(LoginRequiredMixin,CreateView):
      
      model = Destinos
      template_name = "AppTerEnt/create.html"
      success_url = reverse_lazy("Listdest")
      fields = ["city", "country", "category", "popularity"]

class AtraccionesCreateView(LoginRequiredMixin,CreateView):
      
      model = Atracciones
      template_name = "AppTerEnt/create.html"
      success_url = reverse_lazy("Listatr")
      fields = ["name", "city", "category"]

class AlojamientosCreateView(LoginRequiredMixin,CreateView):
      
      model = Alojamientos
      template_name = "AppTerEnt/create.html"
      success_url = reverse_lazy("Listal")
      fields = ["name", "city", "country", "adress", "stars"]

class ActividadesCreateView(LoginRequiredMixin,CreateView):
      
      model = Actividades
      template_name = "AppTerEnt/create.html"
      success_url = reverse_lazy("Listact")
      fields = ["name", "difficulty", "duration"]

#Clases para actualizar registros en las diferentes tablas de la BD.

class DestinosUpdateView(LoginRequiredMixin,UpdateView):
      
      model = Destinos
      template_name = "AppTerEnt/edit.html"
      success_url = reverse_lazy("Listdest")
      fields = ["city", "country", "category", "popularity"]

class AtraccionesUpdateView(LoginRequiredMixin,UpdateView):
      
      model = Atracciones
      template_name = "AppTerEnt/edit.html"
      success_url = reverse_lazy("Listatr")
      fields = ["name", "city", "category"]

class AlojamientosUpdateView(LoginRequiredMixin,UpdateView):
      
      model = Alojamientos
      template_name = "AppTerEnt/edit.html"
      success_url = reverse_lazy("Listal")
      fields = ["name", "city", "country", "adress", "stars"]

class ActividadesUpdateView(LoginRequiredMixin,UpdateView):
      
      model = Actividades
      template_name = "AppTerEnt/edit.html"
      success_url = reverse_lazy("Listact")
      fields = ["name", "difficulty", "duration"]

#Clases para eliminar registros en las diferentes tablas de la BD.

class DestinosDeleteView(LoginRequiredMixin,DeleteView):
      
      model = Destinos
      template_name = "AppTerEnt/confirm_delete.html"
      success_url = reverse_lazy("Listdest")

class AtraccionesDeleteView(LoginRequiredMixin,DeleteView):
      
      model = Atracciones
      template_name = "AppTerEnt/confirm_delete.html"
      success_url = reverse_lazy("Listatr")

class AlojamientosDeleteView(LoginRequiredMixin,DeleteView):
      
      model = Alojamientos
      template_name = "AppTerEnt/confirm_delete.html"
      success_url = reverse_lazy("Listal")

class ActividadesDeleteView(LoginRequiredMixin,DeleteView):
      
      model = Actividades
      template_name = "AppTerEnt/confirm_delete.html"
      success_url = reverse_lazy("Listact")


