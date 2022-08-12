from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
# Create your views here.
from AppCoder.models import Curso


def curso(request, nombre, camada):
    cur = Curso(nombre=nombre, camada=camada)
    cur.save()
    plantilla = loader.get_template('curso.html')
    contexto = {
        "nombre": cur.nombre,
        "camada": cur.camada
    }
    documento = plantilla.render(contexto)

    return HttpResponse(documento)
