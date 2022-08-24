from django.http import HttpResponse
from django.shortcuts import render, redirect

from AppCoder.forms import CursoForm, BuscaCurso
from AppCoder.models import Curso


def buscar_curso(request):

    curso_buscar = []
    if request.method == "POST":
        camada = request.POST.get('camada')
        curso_buscar = Curso.objects.filter(camada__icontains=camada)


    contexto = {
        'my_form': BuscaCurso(),
        'cursos': curso_buscar
    }

    return render(request, 'AppCoder/buscar_curso.html', contexto)


def inicio(request):
    return render(request, 'index.html')


def curso_leer(request):
    cursos = Curso.objects.all()
    contexto = {
        'cursos': cursos
    }

    return render(request, 'AppCoder/curso/leer.html', contexto)


def curso_editar(request, camada):
    curso = Curso.objects.get(camada=camada)

    if request.method == 'POST':
        my_form = CursoForm(request.POST)

        if my_form.is_valid():

            data = my_form.cleaned_data

            curso.nombre = data.get('nombre')
            curso.camada = data.get('camada')

            curso.save()

            return redirect('AppCoderCursoLeer')

    curso_form = CursoForm(initial={'nombre': curso.nombre, 'camada': curso.camada})

    contexto = {
        'curso_form': curso_form
    }

    return render(request, 'AppCoder/curso/editar.html', contexto)


def curso_grabar(request):
    if request.method == 'POST':
        curso_form = CursoForm(request.POST)

        if curso_form.is_valid():

            data = curso_form.cleaned_data

            curso_data = Curso(nombre=data.get('nombre'), camada=data.get('camada'))
            curso_data.save()

    return redirect('AppCoderCursoLeer')


def curso_crear(request):

    contexto = {
        'curso_form': CursoForm()
    }
    return render(request, 'AppCoder/curso/crear.html', contexto)


def curso_eliminar(request, camada):

    curso = Curso.objects.get(camada=camada)
    curso.delete()

    return redirect('AppCoderCursoLeer')



def profesores(request):
    return render(request, 'AppCoder/profesores.html')


def estudiantes(request):
    return redirect('AppCoderInicio')


def entregables(request):
    return HttpResponse("Vista entregables")
