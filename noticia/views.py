from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def bienvenida(request):
    return render(request, "inicio.html")

def mi_error_404(request, exception):
    return HttpResponse("<h1>Página no encontrada</h1>", status=404)
