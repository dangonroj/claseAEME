from django.shortcuts import render
from master.models import *
from django.shortcuts import get_object_or_404
from master.forms import *

# vista 1 - inicio. Muestra el listado de asignaturas, profesores y alumnos
def index(request):
    asignaturas = Asignatura.objects.all()
    profesores = Profesor.objects.all()
    alumnos = Alumno.objects.all()

    # para ordenar el listado por apellidos
    #alumnos = Alumno.objects.all().order_by('apellidos')

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

# vista 3 - asignatura. Muestra los datos de las asignaturas y el alumnado matriculado con su calificación (si se ha presentado)
def ver_asignatura(request,id):
    asignatura = get_object_or_404(Asignatura,id=id)

    #Acceso a matriculas de esa asignatura
    matriculas = Matricula.objects.filter(asignatura=asignatura)

    return render(request,'asignatura.html',{'asignatura':asignatura, 'matriculas':matriculas})


# vista 4 - formulario para buscar
def buscar_alum(request):
   if request.method == 'GET':
      return render(request, 'buscar_alum.html')
   elif request.method == 'POST':
       form = BuscarAlumForm(request.POST)
       if form.is_valid():
           texto = form.cleaned_data["q"]
           alumnos = Alumno.objects.filter(apellidos__icontains=texto)
           return render(request,'listado_alumnado.html', {'alumnos':alumnos})
       else:
           return HttpResponseRedirect('/master/buscar_alum/')
