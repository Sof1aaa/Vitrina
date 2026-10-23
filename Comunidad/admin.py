from django.contrib import admin

from .models import Iniciativa, Miembro, Miembro_Iniciativa, Ubicacion_Sede, RedSocial, Evento, Miembro_Evento, Galeria_Evento
# Register your models here.
admin.site.register(Iniciativa)
admin.site.register(Miembro)
admin.site.register(Miembro_Iniciativa)
admin.site.register(Ubicacion_Sede)
admin.site.register(RedSocial)
admin.site.register(Evento)
admin.site.register(Miembro_Evento)
admin.site.register(Galeria_Evento)