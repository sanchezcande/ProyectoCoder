from django.urls import path
from AppCoder import views

urlpatterns = [
    path('crear curso', views.crear_curso, name="Crear curso"),
    path('', views.inicio, name="Inicio"),
    path('cursos', views.cursos, name="Cursos"),
    path('profesores', views.profesores, name="Profesores"),
]
