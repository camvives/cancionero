from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_canciones, name='lista_canciones'),
    path('cancion/<int:pk>/', views.cancion_detalle, name='cancion_detalle')
]