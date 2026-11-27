from django import forms
from Comunidad.models import CategoriaIniciativa, Iniciativa, Miembro, GaleriaEvento

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

class IniciativaForm(forms.ModelForm):
    class Meta:
        model = Iniciativa
        fields = [
            'id_categoria',
            'nombre_iniciativa',
            'descripcion_iniciativa',
            'mision_iniciativa',
            'vision_iniciativa',
            'fecha_inicio_iniciativa',
            'universidad_origen_iniciativa',
            'numero_miembros_iniciativa',
            'logo_iniciativa',
            'sitio_web_iniciativa',
            'email_contacto_iniciativa',
        ]
        widgets = {
            'fecha_inicio_iniciativa': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

class GaleriaEventoForm(forms.ModelForm):
    class Meta:
        model = GaleriaEvento
        fields = [
            'id_galeria',
            'imagen_galeria',
            'descripcion_galeria',
            'id_evento'
        ]