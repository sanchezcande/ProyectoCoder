from django.http import HttpRequest
from django.urls import path
from AppCoder import views 
from django.contrib.auth.decorators import login_required

from AppCoder.models import Estudiante
HttpRequest


urlpatterns = [
    path('crear curso', views.crear_curso, name="Crear curso"),
    path('', views.inicio, name="inicio"),
    path('cursos', login_required(views.cursos), name="cursos"),
    # path('profesores', views.profesores, name="profesores"),
    path('entregables', views.entregables, name="entregables"),
    path('cursosFormulario', views.cursos_formulario, name="cursos_formulario"),
    path('busquedaCamada', views.busqueda_camada, name='busqueda_camada'),
    path('buscar', views.buscar, name='buscar'),
    # path('profesores/add', views.profesor_add, name='profesor_add'),
    # path('profesores/delete/<id_profe>', views.profesor_delete, name='profesor_delete'),
    # path('profesores/update/<id_profe>', views.profesor_update, name='profesor_update'),
    path('profesores', views.ProfesorListView.as_view(), name="profesores"),
    path('profesores/add', login_required(views.ProfesorCreateView.as_view()), name="profesor_add"),
    path('profesores/update/<pk>', views.ProfesorUpdateView.as_view(), name='profesor_update'),
    path('profesores/delete/<pk>', views.ProfesorDeleteView.as_view(), name='profesor_delete'),
    path('profesores/view/<pk>', views.ProfesorDetailView.as_view(), name='profesor_view'),
    path('estudiantes', views.estudiantes),
    path('user/avatar/add/', views.agregar_avatar, name='avatar_add')

]
