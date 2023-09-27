from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.decorators import login_required
#from django.http import HttpResponse

#Menú Principal
def inicio(request):
    #user_avatar = Avatar.objects.filter(user=request.user).first()
    #url = user_avatar.imagen.url if user_avatar else None
    return render(request, "app1/inicio.html")#, {"url": url})

#Provincias
@login_required
def provincias(request):
    return render(request, "app1/provincias.html")

#About
def about(request):
    return render(request, "app1/about.html")

def obligatorio(request):
    return render(request, "app1/obligatorio.html")

@login_required
def buenos_aires(request):
    return render(request, "app1/buenos_aires.html")

@login_required
def mendoza(request):
    return render(request, "app1/mendoza.html")

@login_required
def rio_negro(request):
    return render(request, "app1/rio_negro.html")

@login_required
def no_hay_pagina_aun(request):
    return render(request, "app1/no_hay_pagina_aun.html")

#Registro
def register(request):

    if request.method == 'POST':
        
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            
            username = form.cleaned_data['username']
            form.save()
            return render(request, "App1/inicio.html", {"mensaje": "Usuario Creado"})

    else:
        form = UserRegisterForm()

    return render(request, "app1/registro.html", {"form":form})

def login_request(request):
    
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            
            usuario = form.cleaned_data.get('username')
            contras = form.cleaned_data.get('password')
            
            user = authenticate(username=usuario, password=contras)
            
            if user is not None:
                login(request, user)
                
                return render(request, 'app1/inicio.html', {'mensaje': f"Bienvenido {usuario}"})
            else:
                return render(request, 'app1/inicio.html', {'mensaje': "Error: Usuario o contraseña incorrectos."})
        else:
                return render(request, 'app1/inicio.html', {'mensaje': "Error: Datos no válidos."})
    
    form = AuthenticationForm()
    
    return render(request, 'app1/login.html', {'form': form})


#Perfil
@login_required

def editarPerfil(request):
    usuario = request.user

    try:
        avatar_instance = Avatar.objects.get(user=usuario)
    except Avatar.DoesNotExist:
        avatar_instance = None

    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST, request.FILES)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']
            usuario.save()

            password1 = informacion['password1']
            password2 = informacion['password2']

            if password1 and password2 and password1 == password2:
                usuario.set_password(password1)
                usuario.save()

            avatar_image = informacion['avatar_image']
            if avatar_image:
                # Update or create the avatar instance for the user
                if avatar_instance:
                    avatar_instance.imagen = avatar_image
                    avatar_instance.save()
                else:
                    avatar_instance = Avatar(user=usuario, imagen=avatar_image)
                    avatar_instance.save()

            return render(request, 'app1/inicio.html')  # Redirect to the user's profile page

    else:
        initial_data = {
            'email': usuario.email,
        }
        if avatar_instance:
            initial_data['avatar_image'] = avatar_instance.imagen
        miFormulario = UserEditForm(initial=initial_data)

    return render(request, 'app1/perfil.html', {"miFormulario": miFormulario, "usuario": usuario})

#Opiniones comentadas
@login_required
def opiniones(request):
    if request.method == 'POST':
        form = OpinionForm(request.POST)
        if form.is_valid():
            provincia_seleccionada = form.cleaned_data['provincia']
            lugar_turistico = form.cleaned_data['lugar_turistico']
            comentario = form.cleaned_data['comentario']
            
            # Crear y guardar la opinión en la base de datos
            opinion = Opinion(
                provincia=provincia_seleccionada,
                lugar_turistico=lugar_turistico,
                comentario=comentario
            )
            opinion.save()
            opinions = Opinion.objects.all()  # Fetch all opinions from the database
            return render(request, 'app1/opiniones.html', {'form': form, 'opinion': opinions})
    else:
        form = OpinionForm()
        opinions = Opinion.objects.all()  # Fetch all opinions from the database
        
    return render(request, 'app1/opiniones.html', {'form': form, 'opinion': opinions})


def isAdmin(User):
    return User.is_superuser

@login_required
def eliminarCuenta(request):
    return render(request, 'app1/eliminarCuenta.html')

@login_required
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        return render(request, 'app1/inicio.html')  # Redirect to an appropriate page after deletion

    return render(request, 'cuentaEliminada.html')