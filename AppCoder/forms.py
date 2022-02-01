from django.forms import Form, CharField, ImageField, IntegerField, EmailField
class CursoForm(Form):
    curso= CharField()
    camada= IntegerField()
    
# class ProfesorForm(Form):
#     nombre= CharField(max_length=30)
#     apellido= CharField(max_length=30)
#     email= EmailField()
#     profesion= CharField(max_length=30)
     
class AvatarFormulario(Form):
    imagen = ImageField(required=True)