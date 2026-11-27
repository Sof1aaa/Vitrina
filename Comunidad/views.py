from django.shortcuts import render
from Comunidad.models import Evento, Iniciativa, Pais, CategoriaIniciativa, Miembro, Ciudad, RedSocial, Sede, GaleriaEvento, MiembroIniciativa, IniciativaEvento, MiembroEvento
from django.shortcuts import render, get_object_or_404, redirect
from Comunidad.forms import CategoriaForm, MiembroForm, IniciativaForm

# Create your views here.
def listadoPaises(request):
    paises = Pais.objects.all() #Select * from
    return render(request, 'paises/listado_paises.html', {'paises': paises})

def listadoCategorias(request):
    categorias = CategoriaIniciativa.objects.all() #Select * from 
    return render(request, 'CategoriasIniciativas/listado_categorias.html', {'categorias': categorias})

def detalleCategoria(request, id):
    categoria = get_object_or_404( CategoriaIniciativa,id_categoria=id)
    return render(request,'CategoriasIniciativas/detalle_categoria.html',{'categoria': categoria}
    )

def registrarCategoria(request):
# Se define la función registrarCategoria(), que recibe el parámetro request.
# Este contiene la información de la petición HTTP realizada por el usuario.

    if request.method == 'POST':
        formulario = CategoriaForm(request.POST, request.FILES)

        if formulario.is_valid():
            formulario.save()
            return redirect('listado_categorias')
    else:
        formulario = CategoriaForm()

    return render(request,'CategoriasIniciativas/registrar_categoria.html',
        {'formulario': formulario}
    )

def listadoMiembros(request):
    miembros = Miembro.objects.all() #Select * from
    return render(request, 'Miembros/listado_miembros.html', {'miembros': miembros})

def detalleMiembro(request, id):
    miembro = get_object_or_404( Miembro,id_miembro=id)
    return render(request,'Miembros/detalle_miembro.html',{'miembro': miembro}
    )

def registrarMiembro(request):
# Se define la función registrarMiembro(), que recibe el parámetro request.
# Este contiene la información de la petición HTTP realizada por el usuario.

    if request.method == 'POST':
        formulario = MiembroForm(request.POST, request.FILES)

        if formulario.is_valid():
            formulario.save()
            return redirect('listado_miembros')
    else:
        formulario = MiembroForm()

    return render(request,'Miembros/registrar_miembro.html',
        {'formulario': formulario}
    )

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

def detalleIniciativa(request, id):
    iniciativa = get_object_or_404(Iniciativa, id_iniciativa=id)
    return render(request, 'Iniciativas/detalleIniciativa.html', {'iniciativa': iniciativa})

def registrarIniciativa(request):
# Se define la función registrarIniciativa(), que recibe el parámetro request.
# Este contiene la información de la petición HTTP realizada por el usuario.

    if request.method == 'POST':
        formulario = IniciativaForm(request.POST, request.FILES)

        if formulario.is_valid():
            formulario.save()
            return redirect('listado_iniciativas')
    else:
        formulario = IniciativaForm()

    return render(request,'Iniciativas/registrarIniciativa.html',
        {'formulario': formulario}
    )

def listadoGaleriaEvento(request):
    galeria_evento = GaleriaEvento.objects.all()
    return render(request, 'GaleriaEvento/listado_galeria_evento.html', {'galeria_evento': galeria_evento})

def listadoMiembroIniciativa(request):
    miembros_iniciativas = MiembroIniciativa.objects.select_related('id_miembro', 'id_iniciativa').all()
    return render(request, 'MiembrosIniciativas/listado_miembros_iniciativas.html', {
        'miembros_iniciativas': miembros_iniciativas
    })

def listadoIniciativaEvento(request):
    iniciativas_eventos = IniciativaEvento.objects.select_related('id_iniciativa', 'id_evento').all()
    return render(request, 'IniciativaEvento/listado_iniciativa_evento.html', {
        'iniciativas_eventos': iniciativas_eventos
    })

def listadoMiembroEvento(request):
    miembros_eventos = MiembroEvento.objects.select_related('id_miembro', 'id_evento').all()
    return render(request, 'MiembroEvento/listado_miembro_evento.html', {
        'miembros_eventos': miembros_eventos
    })