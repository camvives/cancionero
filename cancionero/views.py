from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Cancion, Setlist

# Create your views here.
def lista_canciones(request):
    canciones = Cancion.objects.all()
    return render(request, 'cancionero/canciones_lista.html', {'canciones': canciones})

def cancion_detalle(request, pk):
    cancion = get_object_or_404(Cancion, pk=pk)
    return render(request, 'cancionero/cancion_detalle.html', {'cancion': cancion})

@login_required
def subir_medio_view(request, cancion_id):
    cancion = get_object_or_404(Cancion, id=cancion_id)
    cancion.subir_medio()
    cancion.save()

    return render(request, 'cancionero/cancion_detalle.html', {'cancion': cancion})

@login_required
def bajar_medio_view(request, cancion_id):
    cancion = get_object_or_404(Cancion, id=cancion_id)
    cancion.bajar_medio()
    cancion.save()

    return render(request, 'cancionero/cancion_detalle.html', {'cancion': cancion})

def setlists(request):
    setlists = Setlist.objects.all()
    return render(request, 'cancionero/setlists.html', {'setlists': setlists})

def setlist_detalle(request, pk):
    setlist = get_object_or_404(Setlist, pk=pk)
    canciones = setlist.canciones.all()
    return render(request, 'cancionero/setlist_detalle.html', {'canciones': canciones})
