from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppCoder.models import *

def crear_curso(request, camada):
    curso = Curso(nombre= 'Python', camada = camada)
    curso.save()
    return HttpResponse (f'Curso creado! {camada}')

def inicio(request):
    return  render(request, '/Users/mac/Desktop/Coderhouse_Python/git/ProyectoCoder/clase18/templates/inicio.html')

def cursos(request):
    return render(request, '/Users/mac/Desktop/Coderhouse_Python/git/ProyectoCoder/clase18/templates/cursos.html')

def profesores(request):
      return render(request, "AppCoder/profesores.html")


def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")


def entregables(request):
    return render(request, "AppCoder/entregables.html")

