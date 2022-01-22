from django.urls import path
from AppCoder import views 

urlpatterns = [
    path('crear curso', views.crear_curso, name="Crear curso"),
    path('', views.inicio, name="Inicio"),
    path('cursos', views.cursos, name="Cursos"),
    path('profesores', views.profesores, name="Profesores"),
    path('entregables', views.entregables, name="Entregables"),
    path('cursosFormulario', views.cursos_formulario, name="cursos_formulario"),
    path('busquedaCamada', views.busqueda_camada, name='busqueda_camada'),
    path('buscar', views.buscar, name='buscar')
]
