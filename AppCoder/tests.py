from django.test import TestCase

from AppCoder.models import Profesor

class ProfesorTestCase(TestCase):

    def test_crear_un_profesor(self):
        profesor = Profesor(nombre='Martín', apellido='Gotelli',
        email='martingotelli@a.com', profesion='Profesor de Python')

        profesor.save()
        
        profesor_en_base = Profesor.objects.get(id=profesor.id)

        self.assertEquals(profesor_en_base.nombre, 'Martín')
        self.assertEquals(profesor_en_base.apellido, 'Gotelli')
        self.assertEquals(profesor_en_base.email, 'martingotelli@a.com')
        self.assertEquals(profesor_en_base.profesion, 'Profesor de Python')