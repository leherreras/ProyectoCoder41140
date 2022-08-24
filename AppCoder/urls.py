from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('', inicio, name='AppCoderInicio'),
    path('profesores', profesores, name='AppCoderProfesores'),
    path('estudiantes', estudiantes),
    # urls curso
    path('curso/', curso_leer, name='AppCoderCursoLeer'),
    path('curso/crear', curso_crear, name='AppCoderCursoCrear'),
    path('curso/grabar', curso_grabar, name='AppCoderCursoGrabar'),
    path('curso/eliminar/<int:camada>', curso_eliminar, name='AppCoderCursoEliminar'),
    path('curso/editar/<int:camada>', curso_editar, name='AppCoderCursoEditar')
]
