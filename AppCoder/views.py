from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso

def crear_curso(request, camada):
    curso = Curso(nombre= 'Python', camada = camada)
    curso.save()
    return HttpResponse (f'Curso creado! {camada}')

def inicio(request):
   
    return  render(request, '/Users/mac/Desktop/Coderhouse_Python/git/ProyectoCoder/templates/inicio.html')

def cursos(request):
    
    return render(request, '/Users/mac/Desktop/Coderhouse_Python/git/ProyectoCoder/templates/cursos.html')

def profesores(request):
    return HttpResponse('profesores')


def estudiantes(request):
    return HttpResponse('estudiantes')


def entregables(request):
    return HttpResponse('entregables')

