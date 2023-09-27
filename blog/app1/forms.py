from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import *
#class RegistroFormulario(forms.Form):
    #nickname = forms.CharField()
    #first_name = forms.CharField()
    #last_name = forms.CharField()
    #email = forms.EmailField()
    #password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')
    
class SignInForm(forms.Form):
    nickname = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
class UserRegisterForm(UserCreationForm):
    
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
    first_name = forms.CharField()
    last_name = forms.CharField()
    
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2', 'first_name', 'last_name']
        help_texts = {k:"" for k in fields}
        
class UserEditForm(forms.ModelForm):
    email = forms.EmailField(label="Modificar correo.")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label="Repetir la contraseña", widget=forms.PasswordInput, required=False)
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    avatar_image = forms.ImageField(label="Subir imagen de avatar", required=False)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name', 'avatar_image']
        help_texts = {k: "" for k in fields}

class OpinionForm(forms.ModelForm):
    class Meta:
        model = Opinion
        fields = ['provincia', 'lugar_turistico', 'comentario']