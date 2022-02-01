from tabnanny import verbose
from django.db.models import Model, ForeignKey, CASCADE, ImageField
from django.db.models.fields import CharField, IntegerField, DateField, BooleanField, EmailField
from django.contrib.auth.models import User

class Curso(Model):

    nombre= CharField(max_length=40, verbose_name='Descripcion del curso')
    camada = IntegerField()
    
    def __str__(self):
        return f'Curso {self.nombre} ({self.camada})'

class Estudiante(Model):
    nombre= CharField(max_length=30)
    apellido= CharField(max_length=30)
    email= EmailField()

class Profesor(Model):
    nombre= CharField(max_length=30)
    apellido= CharField(max_length=30)
    email= EmailField()
    profesion= CharField(max_length=30)
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}({self.email}). Profe de {self.profesion} '

class Entregables(Model):
    nombre= CharField(max_length=30)
    fechaDeEntrega = DateField()  
    entregado = BooleanField()

class Avatar(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    imagen = ImageField(upload_to='avatares', null=True, blank=True)
    