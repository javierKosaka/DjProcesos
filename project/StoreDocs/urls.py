from django.urls import path

from . import views

app_name = 'StoreDocs'

urlpatterns = [
    path('ListadoDocumentos/', views.ListadoDocumentos, name='ListadoDocumentos'),
    path('CrearDocumentos/', views.CrearDocumentos, name='CrearDocumentos'),
    path('DetalleDocumentos/<int:pk>', views.DetalleDocumentos, name='DetalleDocumentos'),
    path('UpdateDocumentos/<int:pk>', views.UpdateDocumentos, name='UpdateDocumentos'),
    path('DeleteDocumentos/<int:pk>', views.DeleteDocumentos, name='DeleteDocumentos'),
]
