from django.forms import ModelForm
from .models import curso

class RegistrarCurso(ModelForm):
    class Meta:
        model = curso
        fields = ['titulo', 'eleccion_curso', 'descripcion', 'fecha_inscripcion', 'creador']
        
        