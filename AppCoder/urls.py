from django.urls import path
from AppCoder.views import inicio, cursos, profesores, estudiantes

urlpatterns = [
    path('', inicio, name='AppCoderInicio'),
    path('cursos', cursos, name='AppCoderCursos'),
    path('profesores', profesores, name='AppCoderProfesores'),
    path('estudiantes', estudiantes)
]
