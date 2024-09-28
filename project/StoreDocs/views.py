from django.shortcuts import render, redirect 
from .models import BaseDocs
from .forms import CrearDocumentosForm

def ListadoDocumentos(request):
    documentos = BaseDocs.objects.all()
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
    return render(request, "StoreDocs/CrearDocumentos.html", {"form" : form})
    


