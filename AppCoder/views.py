from django.http import HttpResponse
from django.shortcuts import render, redirect

from AppCoder.dtos import curso_dto


def inicio(request):
    return render(request, 'index.html')


def cursos(request):

    return render(request, 'AppCoder/cursos.html', curso_dto)


def profesores(request):
    return render(request, 'AppCoder/profesores.html')


def estudiantes(request):
    return redirect('AppCoderInicio')


def entregables(request):
    return HttpResponse("Vista entregables")
