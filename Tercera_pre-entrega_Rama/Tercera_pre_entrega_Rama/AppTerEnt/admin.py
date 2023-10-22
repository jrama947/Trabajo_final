from django.contrib import admin
from .models import Destinos, Actividades, Atracciones, Alojamientos

# Register your models here.
admin.site.register(Destinos)
admin.site.register(Actividades)
admin.site.register(Atracciones)
admin.site.register(Alojamientos)