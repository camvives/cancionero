from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_canciones, name='lista_canciones'),
    path('cancion/<int:pk>/', views.cancion_detalle, name='cancion_detalle'),
    path('cancion/<int:cancion_id>/subir/', views.subir_medio_view, name='subir_medio'),
    path('cancion/<int:cancion_id>/bajar/', views.bajar_medio_view, name='bajar_medio'),
    path('setlists', views.setlists, name='setlists'),
    path('setlist/<int:pk>/', views.setlist_detalle, name='setlist_detalle')

]