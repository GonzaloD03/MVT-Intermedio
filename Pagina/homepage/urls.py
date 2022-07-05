from django.urls import path

from homepage import views

urlpatterns = [
  path('', views.inicio, name="Inicio"),
  path('añadir', views.añadir, name="Añadir"),
  path('buscador', views.buscador, name="Buscador"),
  path('buscar/', views.buscar),
]