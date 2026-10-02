from django.contrib import admin
from .models import PerfilUsuario, Publicacion, HistorialEstado, Interaccion

# Register your models here.
admin.site.register(PerfilUsuario)
admin.site.register(Publicacion)
admin.site.register(HistorialEstado)
admin.site.register(Interaccion)