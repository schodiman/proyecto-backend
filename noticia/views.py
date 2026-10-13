from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

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
@login_required
def inicio(request):
    return render(request, 'inicio.html')

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registro exitoso. ¡Bienvenido!')
            return redirect('/')
    else:
        messages.error(request, 'No ha sido posible registrarlo. Por favor revise el formulario.')
    return render(request, 'registration/registro.html', {'form': form})

def mi_error_404(request, exception):
    return render(request, 'registration/404.html', status=404)

class PerfilUsuarioViewSet(viewsets.ModelViewSet):
    queryset = PerfilUsuario.objects.all()
    serializer_class = PerfilUsuarioSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    
class PublicacionViewSet(viewsets.ModelViewSet):
    queryset = Publicacion.objects.all()
    serializer_class = PublicacionSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

class HistorialEstadoViewSet(viewsets.ModelViewSet):
    queryset = HistorialEstado.objects.all()
    serializer_class = HistorialEstadoSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]  

class InteraccionViewSet(viewsets.ModelViewSet):
    queryset = Interaccion.objects.all()
    serializer_class = InteraccionSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    
class VistaProtegida(LoginRequiredMixin, TemplateView):
    template_name = 'inicio.html'
    login_url = '/login/'      