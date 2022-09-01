from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect

from UserCoder.forms import UserRegisterForm, AvatarForm
from UserCoder.models import Avatar


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data

            usuario = data.get('username')
            contrasenia = data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user:
                login(request, user)
                messages.info(request, 'Inicio de sesion satisfactorio!')

            else:
                messages.info(request, 'inicio de sesion fallido!')
        else:
            messages.info(request, 'inicio de sesion fallido!')

        return redirect('AppCoderInicio')

    contexto = {
        'form': AuthenticationForm(),
        'name_submit': 'Login'
    }
    return render(request, 'UserCoder/login.html', contexto)


def register(request):

    if request.method == 'POST':

        form = UserRegisterForm(request.POST, request.FILES)

        if form.is_valid():

            user = form.save()

            avatar = Avatar(user=user, imagen=form.cleaned_data.get('imagen'))
            avatar.save()

            messages.info(request, 'Tu usuario fue registrado satisfactoriamente!')
        else:
            messages.info(request, 'Tu usuario no puso ser registrado!')
        return redirect('AppCoderInicio')

    contexto = {
        # 'form': UserCreationForm(),
        'form': UserRegisterForm(),
        'name_submit': 'Registrarse'
    }

    return render(request, 'UserCoder/login.html', contexto)


def upload_avatar(request):
    if request.method == "POST":

        formulario = AvatarForm(request.POST, request.FILES)

        if formulario.is_valid():

            data = formulario.cleaned_data
            avatar = Avatar.objects.filter(user=data.get("usuario"))

            if len(avatar) > 0:
                avatar = avatar[0]
                avatar.imagen = formulario.cleaned_data["imagen"]
                avatar.save()

            else:
                avatar = Avatar(user=data.get("user"), imagen=data.get("imagen"))
                avatar.save()

        return redirect("AppCoderInicio")

    contexto = {
        "form": AvatarForm()
    }
    return render(request, "UserCoder/avatar.html", contexto)
