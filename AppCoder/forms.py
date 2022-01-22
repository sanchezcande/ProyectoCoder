from django.forms import Form, CharField, IntegerField

class CursoForm(Form):
    curso= CharField()
    camada= IntegerField()