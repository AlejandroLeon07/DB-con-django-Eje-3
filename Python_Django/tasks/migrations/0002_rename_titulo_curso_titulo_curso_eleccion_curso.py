# Generated by Django 5.1.3 on 2024-11-09 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curso',
            old_name='Titulo',
            new_name='titulo',
        ),
        migrations.AddField(
            model_name='curso',
            name='eleccion_curso',
            field=models.CharField(choices=[('Programación', 'Programación'), ('Administración', 'Administración'), ('Contaduría', 'Contaduría'), ('Cocina', 'Cocina'), ('Gestión ambiental', 'Gestión ambiental'), ('Otros', 'Otros'), ('Seleccione una opción', 'Seleccione una opción')], default='Seleccione una opción', max_length=100),
        ),
    ]
