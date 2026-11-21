from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

<<<<<<< Updated upstream
from Comunidad.views import listadoPaises, listadoCategorias
=======
from Comunidad.views import listadoPaises, listadoCategorias, listadoMiembros, listadoCiudades, listadoSedes, listadoEventos, listadoRedesSociales, listadoIniciativas, listadoGaleriaEvento
>>>>>>> Stashed changes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('paises/', listadoPaises, name='listado_paises'),
<<<<<<< Updated upstream
    path('categorias/', listadoCategorias, name='listado_categorias')
=======
    path('categorias/', listadoCategorias, name='listado_categorias'),
    path('miembros/', listadoMiembros, name='listado_miembros'),
    path('ciudades/', listadoCiudades, name='listado_ciudades'),
    path('sedes/', listadoSedes, name='listado_sedes'),
    path('eventos/', listadoEventos, name='listado_eventos'),
    path('redes-sociales/', listadoRedesSociales, name='listado_redes_sociales'),
    path('iniciativas/', listadoIniciativas, name='listado_iniciativas'),
    path('galeria-eventos/', listadoGaleriaEvento, name='listado_galeria_evento')
>>>>>>> Stashed changes
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )