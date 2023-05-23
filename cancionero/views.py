from django.shortcuts import render
from .models import Cancion

# Create your views here.
def lista_canciones(request):
    canciones = Cancion.objects.all()
    return render(request, 'cancionero/canciones_lista.html', {'canciones': canciones})