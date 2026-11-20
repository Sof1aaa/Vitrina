from django.shortcuts import render
from Comunidad.models import Pais, CategoriaIniciativa, Miembro, Ciudad

# Create your views here.
def listadoPaises(request):
    paises = Pais.objects.all() #Select *
    return render(request, 'paises/listado_paises.html', {'paises': paises})

def listadoCategorias(request):
    categorias = CategoriaIniciativa.objects.all() #Select * from 
    return render(request, 'CategoriasIniciativas/listado_categorias.html', {'categorias': categorias})

def listadoMiembros(request):
    miembros = Miembro.objects.all() #Select * from
    return render(request, 'Miembros/listado_miembros.html', {'miembros': miembros})

# JOIN ENTRE DOS TABLAS USANDO ORM DJANGO
def listadoCiudades(request):
    ciudades = Ciudad.objects.select_related('id_pais')
    return render(request, 'Ciudades/listado_ciudades.html', {'ciudades': ciudades})