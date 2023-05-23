from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_canciones, name='lista_canciones')
]