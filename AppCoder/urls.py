from django.urls import path
from AppCoder.views import inicio, curso, profesores, estudiantes

urlpatterns = [
    path('', inicio, name='AppCoderInicio'),
    path('curso', curso, name='AppCoderCurso'),
    path('profesores', profesores, name='AppCoderProfesores'),
    path('estudiantes', estudiantes)
]
