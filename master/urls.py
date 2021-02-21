# Archivo creado para el ejemplo 5
from django.conf.urls import url
from django.urls import path
from . import views
app_name = 'master'

urlpatterns = [
    # vista 1 - inicio. Muestra el listado de asignaturas, profesores y alumnos
    path('', views.index, name='index'),

    # vista 2 - perfil de alumno
    url('alum/(?P<id>\d+)/', views.ver_alum)
]