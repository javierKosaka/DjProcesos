from django.db import models

# Create your models here.

class BaseDocs(models.Model):
    # Definir DOCUMENTO
    DOCUMENTO = models.CharField(max_length=100, unique=True)
    
    # Definir TIPO_DOCUMENTO (limitar a opciones validadas)
    TIPO_DOCUMENTO_OPCIONES = [
        ('MANUAL DE PROCESOS', 'Manual de procesos'),
        ('PROCEDIMIENTO', 'Procedimiento'),
        ('FORMULARIO', 'Formularios')
    ]
    TIPO_DOCUMENTO = models.CharField(max_length=30, choices=TIPO_DOCUMENTO_OPCIONES)
    
    # Definir DESCRIPCION
    DESCRIPCION = models.TextField(null=True, blank=True)
    
    # Definir INICIO_VIGENCIA
    INICIO_VIGENCIA = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.DOCUMENTO

    class Meta:
        verbose_name = 'Base de documento'
        verbose_name_plural = 'Base de documentos'