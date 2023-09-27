from django.db import models

#Provincias
class Provincia(models.Model):
    nombre = models.CharField(max_length=100)
    num_localidades = models.CharField(max_length=2, unique=True) #Cantidad de localidades turisticas que tiene

    def __str__(self):
        return self.nombre

class LocalidadTuristica(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=4, unique=True)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE, related_name='localidades_turisticas')

    def __str__(self):
        return self.nombre


#Caja de comentarios para users
class Comentario(models.Model):
    comentario = models.ForeignKey(Provincia, related_name='comentarios', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=50)
    mensaje = models.TextField(null=True, blank=True)
    fechaComentario = models.DateTimeField(auto_now_add=True)

    class Meta: #ordena por fecha de comentario
        ordering = ['-fechaComentario']

    def __str__(self): #ordena primero indicando el nombre, luego el comentario.
        return '%s - %s' % (self.nombre, self.comentario)

