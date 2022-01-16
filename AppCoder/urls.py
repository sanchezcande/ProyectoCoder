
from django.urls import path
from AppCoder.views import crear_curso, inicio, cursos

urlpatterns = [
    path('crearcurso/<camada>', crear_curso),
    path('', inicio),
    path('cursos', cursos),
]
