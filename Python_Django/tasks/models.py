from django.db import models
from django.contrib.auth.models import User

# Create your models here.
Cursos_disponibles = [
        ('Programación', 'Programación'),
        ('Administración', 'Administración'),
        ('Contaduría', 'Contaduría'),
        ('Cocina', 'Cocina'),
        ('Gestión ambiental', 'Gestión ambiental'),
        ('Otros', 'Otros'),
        ('Seleccione una opción', 'Seleccione una opción'),
    ]

class curso(models.Model):
    titulo = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    eleccion_curso = models.CharField(max_length=100, choices=Cursos_disponibles, default='Seleccione una opción')
    descripcion = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_inscripcion = models.DateTimeField(null=True)
    creador = models.CharField(max_length=100)
    
    def __str__(self):
        return 'INSCRIPCIÓN AL CURSO ' + self.eleccion_curso + '- by ' + self.user.username 

