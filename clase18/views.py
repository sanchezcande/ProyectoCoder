from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from clase18.forms import UserEditForm, UserRegisterForm
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required




def login_request (request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data['username']
            contraseña = form.cleaned_data['password']
            user = authenticate(username=usuario, password=contraseña)
            
            if user is not None:
                login(request, user)
                return redirect('inicio')
            else:
                return redirect(request, 'login.html', 
                            {'form': form,
                             'error': 'No es válido el usuario y contraseña' })  #Este código se podría ignorar

        else:
            return render(request, 'login.html', {'form': form})
        
    else:
        form=AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    

# def register(request):
#     if request.method=="POST":
#             form = UserRegisterForm(request.POST)
            
#             if form.is_valid():
#                 username= form.cleaned_data['username']
#                 form.save()
#                 return HttpResponse(f'Usuario {username} creado correctamente')
            
#     else:
#         form= UserRegisterForm()
        
#     return render(request, 'register.html', {'form': form})

class UserCreateView(CreateView):
    model=User
    success_url = reverse_lazy('login')
    template_name = 'register.html'
    form_class = UserRegisterForm
    
@login_required
def editar_perfil(request):
    usuario = request.user
    
    if request.method == "POST":
        formulario= UserEditForm(request.POST)
        if formulario.is_valid():
            data=formulario.cleaned_data
            usuario.email=data['email']
            usuario.set_password(data['password1'])
            usuario.first_name=data['first_name']
            usuario.last_name=data['last_name']
            usuario.save()
            return redirect('inicio')

            
    else:
        formulario = UserEditForm ({'email': usuario.email})
        
    return render(request, 'register.html', {'form': formulario})