from django.urls import path

from . import views

app_name = 'StoreDocs'

urlpatterns = [
    path('ListadoDocumentos/', views.ListadoDocumentos, name='ListadoDocumentos'),
    path('CrearDocumentos/', views.CrearDocumentos, name='CrearDocumentos'),
]
