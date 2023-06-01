from django.shortcuts import render, get_object_or_404, redirect
from .models import Cancion

# Create your views here.
def lista_canciones(request):
    canciones = Cancion.objects.all()
    return render(request, 'cancionero/canciones_lista.html', {'canciones': canciones})

def cancion_detalle(request, pk):
    cancion = get_object_or_404(Cancion, pk=pk)
    return render(request, 'cancionero/cancion_detalle.html', {'cancion': cancion})


def subir_medio_view(request, cancion_id):
    cancion = get_object_or_404(Cancion, id=cancion_id)
    cancion.subir_medio()
    cancion.save()

    return render(request, 'cancionero/cancion_detalle.html', {'cancion': cancion})

def bajar_medio_view(request, cancion_id):
    cancion = get_object_or_404(Cancion, id=cancion_id)
    cancion.bajar_medio()
    cancion.save()

    return render(request, 'cancionero/cancion_detalle.html', {'cancion': cancion})