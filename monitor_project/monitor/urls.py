from django.urls import path
from . import views

urlpatterns = [
    path('api/cantidad_modulos/', views.obtener_cantidad_modulos, name='obtener_cantidad_modulos'),
]