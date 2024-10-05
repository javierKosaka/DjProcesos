from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class BaseDocs(models.Model):
    # Definir DOCUMENTO
    DOCUMENTO = models.CharField(max_length=100, unique=True)
    
    # Definir TIPO_DOCUMENTO (limitar a opciones validadas)
    TIPO_DOCUMENTO_OPCIONES = [
        ('01. MANUAL DE PROCESOS', 'Manual de procesos'),
        ('02. PROCEDIMIENTO', 'Procedimiento'),
        ('03. FORMULARIO', 'Formularios')
    ]
    TIPO_DOCUMENTO = models.CharField(max_length=30, choices=TIPO_DOCUMENTO_OPCIONES)

    
    # Definir DESCRIPCION
    DESCRIPCION = models.TextField(null=True, blank=True)
    
    # Definir INICIO_VIGENCIA
    INICIO_VIGENCIA = models.DateField(null=True, blank=True)
    
    # Definir FIN_VIGENCIA
    FIN_VIGENCIA = models.DateTimeField(
        null=True, 
        blank=True,
        default=None
    )
    
    # Definir VERSION
    VERSION = models.IntegerField(
        default=1,
        validators=[
            MinValueValidator(1)
        ]
    )

    def __str__(self):
        return self.DOCUMENTO

    class Meta:
        verbose_name = 'Base de documento'
        verbose_name_plural = 'Base de documentos'