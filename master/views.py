from django.shortcuts import render
from master.models import *
from django.shortcuts import get_object_or_404


# vista 1 - inicio. Muestra el listado de asignaturas, profesores y alumnos
def index(request):
    asignaturas = Asignatura.objects.all()
    profesores = Profesor.objects.all()
    alumnos = Alumno.objects.all()

    return render(request,'indexMaster.html',{'asignaturas':asignaturas,'profesores':profesores,'alumnos':alumnos})

# vista 2 - alumno. Muestra sus datos personales y las asignaturas en las que se ha matriculado (con su nota si se ha presentado)
def ver_alum(request,id):
    # Acceso básico a datos
    #alum = Alumno.objects.get(id=id)

    # Acceso con control de excepciones
    alum = get_object_or_404(Alumno,id=id)

    # Filtrado de martrículas por alumno
    matriculas = Matricula.objects.filter(alumno=alum)

    return render(request,'alum.html',{'alum':alum, 'matriculas':matriculas})