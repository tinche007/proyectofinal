from django.urls import path
from app1 import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name = "inicio"),
    path('login/', views.login_request, name = "login"),
    path('registro/', views.register, name = "registro"),
    path('perfil/', views.editarPerfil, name = "perfil"),

    path('provincias/', views.provincias, name = "provincias"),
    path('opiniones/', views.opiniones, name = "opiniones"),
    path('obligatorio/', views.obligatorio, name = "obligatorio"),
    path('no_hay_pagina_aun/', views.no_hay_pagina_aun, name = "no_hay_pagina_aun"),

    path('about/', views.about, name = "about"),
    path('logout', LogoutView.as_view(template_name='app1/logout.html'), name= 'logout'),

    path('eliminarCuenta/', views.eliminarCuenta, name='eliminarCuenta'),
    path('cuentaEliminada/', views.delete_account, name='cuentaEliminada'),
    ]

