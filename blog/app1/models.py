from django.db import models
from django.contrib.auth.models import User

#Perfil de usuario
class UserProfile(models.Model):
    nickname = models.CharField(max_length=20, unique = True)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.EmailField(unique = True)
    password = models.CharField(max_length=20, default=123456)

    def __str__(self):
        return self.nickname

#Avatar del usuario  
class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares/', null=True, blank=True)
    
    def __str__(self):
        return f"{self.user} - {self.imagen}"

#Provincias
class Provincia(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='provincias/')

    def __str__(self):
        return self.nombre

#Comentario
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f"Comment by {self.user} on {self.provincia.nombre}"

class Opinion(models.Model):
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
    lugar_turistico = models.CharField(max_length=100)
    comentario = models.TextField()