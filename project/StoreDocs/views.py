from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import BaseDocs
from .forms import CrearDocumentosForm

def ListadoDocumentos(request):
    documentos = BaseDocs.objects.filter(FIN_VIGENCIA__isnull=True).order_by('TIPO_DOCUMENTO')
    context = {'documentos': documentos}
    return render(request, "StoreDocs/ListadoDocumentos.html", context)


def CrearDocumentos(request):
    if request.method == 'GET':
        form = CrearDocumentosForm()
        
    if request.method == 'POST':
        form = CrearDocumentosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("StoreDocs:ListadoDocumentos")
    return render(request, "StoreDocs/FormDocumentos.html", {"form" : form})


def DetalleDocumentos(request, pk: int):
    query = BaseDocs.objects.get(id=pk)
    context = {'object' : query}
    return render(request, "StoreDocs/DetalleDocumentos.html", context)
    
# UPDATE

def UpdateDocumentos(request, pk: int):
    query = BaseDocs.objects.get(id=pk)
    if request.method == 'GET':
        # traer los datos en los campos que figuran en la base
        form = CrearDocumentosForm(instance=query)
        
    if request.method == 'POST':
        form = CrearDocumentosForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect("StoreDocs:ListadoDocumentos")
    return render(request, "StoreDocs/FormDocumentos.html", {"form" : form})


# BORRADO LOGICO

def DeleteDocumentos(request, pk):
    documento = get_object_or_404(BaseDocs, id=pk)
    if request.method == 'POST':
        # AGREGAR FIN VIGENCIA
        documento.FIN_VIGENCIA = timezone.now()
        documento.save()
        return redirect("StoreDocs:ListadoDocumentos")
    else:
        # Mostrar una página de confirmación
        return render(request, "StoreDocs/ConfirmarBorradoDocumentos.html", {"documento": documento})
        