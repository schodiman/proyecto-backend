from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets

from .models import (
PerfilUsuario,
    Publicacion,
    HistorialEstado,
    Interaccion
)

from .serializer import (
PerfilUsuarioSerializer, 
PublicacionSerializer,
HistorialEstadoSerializer,
InteraccionSerializer
)

def inicio(request):
    return HttpResponse("inicio.html")
def mi_error_404(request, exception):
    return HttpResponse("h1>Página no encontrada</h1>", status=404)

class PerfilUsuarioViewSet(viewsets.ModelViewSet):
    queryset = PerfilUsuario.objects.all()
    serializer_class = PerfilUsuarioSerializer
    
class PublicacionViewSet(viewsets.ModelViewSet):
    queryset = Publicacion.objects.all()
    serializer_class = PublicacionSerializer

class HistorialEstadoViewSet(viewsets.ModelViewSet):
    queryset = HistorialEstado.objects.all()
    serializer_class = HistorialEstadoSerializer

class InteraccionViewSet(viewsets.ModelViewSet):
    queryset = Interaccion.objects.all()
    serializer_class = InteraccionSerializer    