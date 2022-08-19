from django.http import HttpResponse
from django.shortcuts import render, redirect

from AppCoder.forms import CursoForm
from AppCoder.models import Curso


def inicio(request):
    return render(request, 'index.html')


def curso(request):

    if request.method == 'POST':
        my_form = CursoForm(request.POST)

        if my_form.is_valid():

            data = my_form.cleaned_data

            curso_data = Curso(nombre=data.get('nombre'), camada=data.get('camada'))
            curso_data.save()

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
