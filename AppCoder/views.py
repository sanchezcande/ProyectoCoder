from ast import Delete
import re
from django.forms import model_to_dict
from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from AppCoder.models import *
from AppCoder.forms import AvatarFormulario, CursoForm
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required



def crear_curso(request, camada):
    curso = Curso(nombre= 'Python', camada = camada)
    curso.save()
    return HttpResponse (f'Curso creado! {camada}')

def inicio(request):
    avatares = Avatar.objects.filter(user=request.user)
    
    if avatares:
        avatar_url = avatares.last().imagen.url
    else: 
        avatar_url = ''
    return  render(request, 'AppCoder/inicio.html', {'avatar_url': avatar_url})
    

def cursos(request):
    return render(request, 'AppCoder/cursos.html',
    {'cursos': Curso.objects.all})


def estudiantes(request):
    return HttpResponse(f'estudiantes')


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
    
def profesores(request):
    return render(request, 
        "AppCoder/profesores.html",
        {'profesores': Profesor.objects.all()}
         )

# def profesor_add(request):
#     if request.method == 'POST':
#         formulario = ProfesorForm(request.POST)
        
#         if formulario.is_valid():
#             data = formulario.cleaned_data
#             Profesor.objects.create(
#                 nombre=data['nombre'], 
#                 apellido=data['apellido'], 
#                 email=data['email'],
#                 profesion=data['profesion']
#                 )
#             return redirect('profesores')
#     else:
#       formulario = ProfesorForm()
#     return render(request, "AppCoder/cursosFormulario.html", {'formulario': formulario})

def profesor_delete(request, id_profe):
    profesor= Profesor.objects.get(id=id_profe)
    profesor.delete()
    return redirect('profesores')

# def profesor_update (request, id_profe):
#     profesor= Profesor.objects.get(id=id_profe)
#     if request.method == 'POST':
#         formulario = ProfesorForm(request.POST)
        
#         if formulario.is_valid():
#             data = formulario.cleaned_data
        
#             profesor.nombre=data['nombre'], 
#             profesor.apellido=data['apellido'], 
#             profesor.email=data['email'],
#             profesor.profesion=data['profesion']
            
#             profesor.save()
            
#             return redirect('profesores')
#     else:
#       formulario = ProfesorForm(model_to_dict(profesor)) 
#     return render(request, "AppCoder/cursosFormulario.html", {'formulario': formulario})

class AvatarView:
    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['avatar_url'] = Avatar.objects.filter(user=self.request.user).last().imagen.url
        return contexto

class ProfesorListView(LoginRequiredMixin, ListView):
    model = Profesor
    template_name = 'AppCoder/profesores.html' 
    context_object_name = 'profesores'   

class ProfesorDetailView(DetailView):
    model = Profesor
    template_name = 'AppCoder/ver_profesor.html' 

class ProfesorCreateView(CreateView):
    model = Profesor
    success_url =  reverse_lazy ('profesores')
    fields = ['nombre', 'apellido', 'email','profesion' ]
    template_name = 'AppCoder/profesor_form.html' 

class ProfesorUpdateView(UpdateView):
    model = Profesor
    success_url =  reverse_lazy ('profesores')
    fields = ['nombre', 'apellido', 'email','profesion' ]
    template_name = 'AppCoder/profesor_form.html' 
 
class ProfesorDeleteView(DeleteView):
    model = Profesor
    success_url = reverse_lazy('profesores')
    template_name = 'AppCoder/profesor_delete.html' 

@login_required
def agregar_avatar(request):
    if request.method == 'POST':
        formulario =AvatarFormulario(request.POST, request.FILES)
        
        if formulario.is_valid():
            avatar = Avatar(user=request.user, imagen=formulario.cleaned_data['imagen'])
            avatar.save()
            return redirect('inicio')
    else:
        formulario= AvatarFormulario()
        
    return render(request, 'AppCoder/crear_avatar.html', {'form': formulario})