from django.shortcuts import render, get_object_or_404
from .models import Cancion

# Create your views here.
def lista_canciones(request):
    canciones = Cancion.objects.all()
    return render(request, 'cancionero/canciones_lista.html', {'canciones': canciones})

def cancion_detalle(request, pk):
    cancion = get_object_or_404(Cancion, pk=pk)
    return render(request, 'cancionero/cancion_detalle.html', {'cancion': cancion})