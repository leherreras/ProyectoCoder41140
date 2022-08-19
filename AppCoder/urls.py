from django.urls import path
from AppCoder.views import inicio, curso, profesores, estudiantes, buscar_curso

urlpatterns = [
    path('', inicio, name='AppCoderInicio'),
    path('curso', curso, name='AppCoderCurso'),
    path('profesores', profesores, name='AppCoderProfesores'),
    path('estudiantes', estudiantes),
    path('buscar', buscar_curso)
]
