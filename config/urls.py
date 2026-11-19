from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from Comunidad.views import listadoPaises, listadoCategorias

urlpatterns = [
    path('admin/', admin.site.urls),
    path('paises/', listadoPaises, name='listado_paises'),
    path('categorias/', listadoCategorias, name='listado_categorias')
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )