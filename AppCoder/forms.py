from django import forms

from AppCoder.models import Curso


class CursoForm(forms.Form):

    nombre = forms.CharField(max_length=40)
    camada = forms.IntegerField()

    class Meta:
        model = Curso


class BuscaCurso(forms.Form):
    camada = forms.IntegerField()
