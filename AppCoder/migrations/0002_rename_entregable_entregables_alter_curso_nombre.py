# Generated by Django 4.0.1 on 2022-01-18 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Entregable',
            new_name='Entregables',
        ),
        migrations.AlterField(
            model_name='curso',
            name='nombre',
            field=models.CharField(max_length=40, verbose_name='Descripcion del curso'),
        ),
    ]
