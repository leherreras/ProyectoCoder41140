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


def curso(request):

    if request.method == 'POST':
        my_form = CursoForm(request.POST)

        if my_form.is_valid():

            data = my_form.cleaned_data

            curso_data = Curso(nombre=data.get('nombre'), camada=data.get('camada'))
            curso_data.save()
        else:
            redirect('AppCoderInicio')

    cursos = Curso.objects.all()
    contexto = {
        'cursos': cursos,
        'my_form': CursoForm()
    }

    return render(request, 'AppCoder/curso.html', contexto)


def profesores(request):
    return render(request, 'AppCoder/profesores.html')


def estudiantes(request):
    return redirect('AppCoderInicio')


def entregables(request):
    return HttpResponse("Vista entregables")
