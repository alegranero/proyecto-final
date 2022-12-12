"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ejemplo.views import (index, saludar_a, sumar, buscar, monstrar_familiares, division, 
                            BuscarFamiliar, AltaFamiliar, ActualizarFamiliar, BorrarFamiliar, FamiliarList, 
                            FamiliarCrear, FamiliarBorrar)

urlpatterns = [
    path('admin/', admin.site.urls), #toma 2 argumentos, un url y una función - genero vista, template, ruta
    path('saludar/', index),
    path('saludar-a/<nombre>/', saludar_a), #todo lo que venga dsp de la barra, entre <> va a pasar a ser inyectado
    path('sumar/<int:a>/<int:b>/', sumar),
    path('buscar/', buscar),
    path('mi-familia/', monstrar_familiares),
    path('division/<int:c>/<int:d>/', division),
    path('mi-familia/buscar', BuscarFamiliar.as_view()), #as_view transforma el path
    path('mi-familia/alta', AltaFamiliar.as_view()), #as_view transforma el path
    path('mi-familia/actualizar/<int:pk>', ActualizarFamiliar.as_view()), # NUEVA RUTA PARA BUSCAR FAMILIAR
    path('mi-familia/borrar/<int:pk>', BorrarFamiliar.as_view()), # NUEVA RUTA PARA BORRAR FAMILIAR
    path('panel-familia/', FamiliarList.as_view()), # NUEVA RUTA 
    path('panel-familia/crear', FamiliarCrear.as_view()), # NUEVA RUTA 
    path('panel-familia/<int:pk>/borrar', FamiliarBorrar.as_view()), # NUEVA RUTA
]
