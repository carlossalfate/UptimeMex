from django.shortcuts import render
from django.http import JsonResponse
from .models import Sucursal
from pythonping import ping

def index(request):
    return render(request, 'index.html')

from monitor.models import Sucursal
from pythonping import ping

def actualizar_estado_sucursales():
    sucursales = Sucursal.objects.all()
    contadorTrue=0
    contadorFalse=0
    for sucursal in sucursales:
        try:
            resultado_ping = ping(sucursal.ip, count=1)
            if resultado_ping.success():
                sucursal.active = True
            else:
                sucursal.active = False
            sucursal.save()
        except Exception as e:
            print(f"Error al hacer ping a {sucursal.sucursal}: {str(e)}")


def obtener_cantidad_modulos(request):
    modulos = Sucursal.objects.all()

    cantidad_encendidos = Sucursal.objects.filter(active=True).count()
    cantidad_apagados = Sucursal.objects.filter(active=False).count()

    data = []
    for modulo in modulos:
        data.append({
            'sucursal': modulo.sucursal,
            'active': modulo.active,
            # Otros campos que desees devolver
        })

    response_data = {
        'modulos': data,
        'cantidad_encendidos': cantidad_encendidos,
        'cantidad_apagados': cantidad_apagados
    }

    return JsonResponse(response_data, safe=False)
