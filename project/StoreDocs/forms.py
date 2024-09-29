from django import forms
from .models import BaseDocs

class CrearDocumentosForm(forms.ModelForm):
    class Meta:
        model = BaseDocs
        fields = ["DOCUMENTO", "TIPO_DOCUMENTO", "DESCRIPCION", "INICIO_VIGENCIA", "VERSION"]
        widgets = {
            'INICIO_VIGENCIA': forms.DateInput(attrs={'type': 'date'}),
        }
        
