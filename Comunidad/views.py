from django.shortcuts import render
from Comunidad.models import Evento, Iniciativa, Pais, CategoriaIniciativa, Miembro, Ciudad, RedSocial, Sede, GaleriaEvento, MiembroIniciativa

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

def listadoSedes(request):
    sedes = Sede.objects.all()
    return render(request, 'Sedes/listado_sedes.html', {'sedes': sedes})

def listadoEventos(request):
    eventos = Evento.objects.all()
    return render(request, 'Eventos/listado_eventos.html', {'eventos': eventos})

def listadoRedesSociales(request):
    redes_sociales = RedSocial.objects.all()
    return render(request, 'RedesSociales/listado_red_social.html', {'redes_sociales': redes_sociales})

def listadoIniciativas(request):
    iniciativas = Iniciativa.objects.all()
    return render(request, 'Iniciativas/listado_iniciativas.html', {'iniciativas': iniciativas})

def listadoGaleriaEvento(request):
    galeria_evento = GaleriaEvento.objects.all()
    return render(request, 'GaleriaEvento/listado_galeria_evento.html', {'galeria_evento': galeria_evento})

#def listadoMiembroIniciativa(request):
    #miembros_iniciativas = MiembroIniciativa.objects.all()
    #return render (request, 'MiembrosIniciativas/listado_miembros_iniciativas.html', {'miembros_iniciativas': miembros_iniciativas})

def listadoMiembroIniciativa(request):
    miembros_iniciativas = MiembroIniciativa.objects.select_related('id_miembro', 'id_iniciativa').all()
    return render(request, 'MiembrosIniciativas/listado_miembros_iniciativas.html', {
        'miembros_iniciativas': miembros_iniciativas
    })