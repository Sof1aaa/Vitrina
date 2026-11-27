from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Comunidad.views import detalleIniciativa, listadoPaises, listadoCategorias, listadoMiembros, listadoCiudades, listadoSedes, listadoEventos, listadoRedesSociales, listadoIniciativas, listadoGaleriaEvento, listadoMiembroIniciativa, listadoIniciativaEvento, listadoMiembroEvento, registrarCategoria, detalleCategoria, detalleMiembro, registrarMiembro, detalleIniciativa, registrarIniciativa

urlpatterns = [
    path('admin/', admin.site.urls),
    path('paises/', listadoPaises, name='listado_paises'),
    path('categorias/', listadoCategorias, name='listado_categorias'),
    path('categorias/detalle/<str:id>/', detalleCategoria, name='detalleCategoria'),
    path('categorias/registrar/', registrarCategoria, name='registrarCategoria'),
    path('miembros/', listadoMiembros, name='listado_miembros'),
    path('miembros/detalle/<str:id>/', detalleMiembro, name='detalleMiembro'),
    path('miembros/registrar/', registrarMiembro, name='registrarMiembro'),
    path('ciudades/', listadoCiudades, name='listado_ciudades'),
    path('sedes/', listadoSedes, name='listado_sedes'),
    path('eventos/', listadoEventos, name='listado_eventos'),
    path('redes-sociales/', listadoRedesSociales, name='listado_redes_sociales'),
    path('iniciativas/', listadoIniciativas, name='listado_iniciativas'),
    path('iniciativas/detalle/<str:id>/', detalleIniciativa, name='detalleIniciativa'),
    path('iniciativas/registrar/', registrarIniciativa, name='registrarIniciativa'),
    path('galeria-eventos/', listadoGaleriaEvento, name='listado_galeria_evento'),
    path('miembros-iniciativas/', listadoMiembroIniciativa, name='listado_miembros_iniciativas'),
    path('iniciativas-eventos/', listadoIniciativaEvento, name='listado_iniciativa_evento'),
    path('miembros-eventos/', listadoMiembroEvento, name='listado_miembro_evento')
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )