from django import forms
from Comunidad.models import CategoriaIniciativa, Miembro

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = CategoriaIniciativa
        fields = [
            'id_categoria', 
            'nombre_categoria',
            'descripcion_categoria', 
        ]

class MiembroForm(forms.ModelForm):
    class Meta:
        model = Miembro
        fields = [
            'id_miembro', 
            'nombre_miembro',
            'ocupacion_cargo_miembro',
            'info_miembro',
            'foto_miembro',
            'correo_miembro',
        ]
