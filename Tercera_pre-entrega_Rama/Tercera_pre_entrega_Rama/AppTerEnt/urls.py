from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('inicio/', inicio, name = "Inicio"),
    path('destinos/', destinos, name = "Destinos"),
    path('atracciones/', atracciones, name = "Atracciones"),
    path('actividades/', actividades, name = "Actividades"),
    path('alojamientos/', alojamientos, name = "Alojamientos"),
    path('formulario/', formulario, name = "Formulario"),
    path('buscar/', buscar, name = "Buscar"),
    path('mostrar/', mostrar, name = "Mostrar"),
    path('welcome/', welcome, name = "Welcome"),
    path('about/', about, name = "About"),
    path('nz/', nz, name = "Nz"),
    path('ind/', ind, name = "Ind"),
    path('jap/', jap, name = "Jap"),
    path('mtcook/', mtcook, name = "Mtcook"),
    path('arrocera/', arrocera, name = "Arrocera"),
    path('bj/', bj, name = "Bj"),
    path('buceo/', buceo, name = "Buceo"),
    path('sama/', sama, name = "Sama"),

    #URL para vistas basadas en clases del modelo Destinos.

    path('clases/listadest/', DestinosListView.as_view(), name ="Listdest"),
    path('clases/detalledest/<int:pk>', DestinosDetalle.as_view(), name ="Detaildest"),
    path('clases/nuevodest/', DestinosCreateView.as_view(), name ="Newdest"),
    path('clases/editardest/<int:pk>', DestinosUpdateView.as_view(), name ="Editdest"),
    path('clases/eliminardest/<int:pk>', DestinosDeleteView.as_view(), name ="Deletedest"),

    #URL para vistas basadas en clases del modelo Actividades.

    path('clases/listaact/', ActividadesListView.as_view(), name ="Listact"),
    path('clases/detalleact/<int:pk>', ActividadesDetalle.as_view(), name ="Detailact"),
    path('clases/nuevoact/', ActividadesCreateView.as_view(), name ="Newact"),
    path('clases/editaract/<int:pk>', ActividadesUpdateView.as_view(), name ="Editact"),
    path('clases/eliminaract/<int:pk>', ActividadesDeleteView.as_view(), name ="Deleteact"),

    #URL para vistas basadas en clases del modelo Alojamientos.

    path('clases/listaal/', AlojamientosListView.as_view(), name ="Listal"),
    path('clases/detalleal/<int:pk>', AlojamientosDetalle.as_view(), name ="Detailal"),
    path('clases/nuevoal/', AlojamientosCreateView.as_view(), name ="Newal"),
    path('clases/editaral/<int:pk>', AlojamientosUpdateView.as_view(), name ="Edital"),
    path('clases/eliminaral/<int:pk>', AlojamientosDeleteView.as_view(), name ="Deleteal"),

    #URL para vistas basadas en clases del modelo Atracciones.

    path('clases/listaatr/', AtraccionesListView.as_view(), name ="Listatr"),
    path('clases/detalleatr/<int:pk>', AtraccionesDetalle.as_view(), name ="Detailatr"),
    path('clases/nuevoatr/', AtraccionesCreateView.as_view(), name ="Newatr"),
    path('clases/editaratr/<int:pk>', AtraccionesUpdateView.as_view(), name ="Editatr"),
    path('clases/eliminaratr/<int:pk>', AtraccionesDeleteView.as_view(), name ="Deleteatr"),

    #URL para login, registro y logout de usuarios.

    path('login/', login_request, name ="Login"),
    path('register/', register, name ="Register"),
    path('logout/', LogoutView.as_view(template_name='AppTerEnt/welcome.html'), name ="Logout"),

    #URL para edición de usuarios registrados.

     path('edituser/', edit, name ="Edituser"),
    





]
    


