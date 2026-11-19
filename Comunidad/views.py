from django.shortcuts import render
from Comunidad.models import Pais, CategoriaIniciativa

# Create your views here.
def listadoPaises(request):
    paises = Pais.objects.all() #Select * from faculty 
    return render(request, 'paises/listado_paises.html', {'paises': paises})

def listadoCategorias(request):
    categorias = CategoriaIniciativa.objects.all() #Select * from faculty 
    return render(request, 'CategoriasIniciativas/listado_categorias.html', {'categorias': categorias})