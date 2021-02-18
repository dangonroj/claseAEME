"""claseAEME URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from holaMundo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Ejemplo 1 - holaMundo
    url('holaMundo/', views.holaMundo),
    # Ejemplo 2 - holaMundo2
    url('holaMundo2/', views.holaMundo2),
    # Ejemplo 3 - calendario
    url('calendario/', views.calendario),
    # Ejemplo 4 - calculadora
    url('calculadora/(?P<a>\d+)/(?P<b>\d+)', views.calculadora)

]
