from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from UserCoder.models import Avatar


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    imagen = forms.ImageField()

    class Meta:
        model = User
        fields = ('username', 'email', 'imagen')


class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = "__all__"

