import re
from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import CursoForm

def crear_curso(request, camada):
    curso = Curso(nombre= 'Python', camada = camada)
    curso.save()
    return HttpResponse (f'Curso creado! {camada}')

def inicio(request):
    return  render(request, 'AppCoder/inicio.html')

def cursos(request):
    return render(request, 'AppCoder/cursos.html',
    {'cursos': Curso.objects.all})

def profesores(request):
      return render(request, "AppCoder/profesores.html")


def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")


def entregables(request):
    return render(request, "AppCoder/entregables.html")

def cursos_formulario(request):
    if request.method == 'POST':
        formulario = CursoForm(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            Curso.objects.create(nombre=data['curso'], camada=data['camada'])
            return redirect('Cursos')
    else:
      formulario = CursoForm()
    return render(request, "AppCoder/cursosFormulario.html", {'formulario': formulario})

def busqueda_camada(request):
    return render(request, 'AppCoder/busquedaCamada.html')

def buscar(request):
    camada= request.GET.get("camada")
    
    if camada: 
        cursos= Curso.objects.filter(camada=camada)
        return render(request, 'AppCoder/buscar.html',
        {'cursos': cursos, 'camada': camada})
    else:
        return HttpResponse('No se envió una camada válida') 