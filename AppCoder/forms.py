from django import forms


class CursoForm(forms.Form):

    nombre = forms.CharField(max_length=40)
    camada = forms.IntegerField()
