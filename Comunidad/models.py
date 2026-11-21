from django.db import models

class Pais(models.Model):
    id_pais = models.CharField(max_length=10, primary_key=True)
    nombre_pais = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id_pais)


class CategoriaIniciativa(models.Model):
    id_categoria = models.CharField(max_length=10, primary_key=True)
    nombre_categoria = models.CharField(max_length=100)
    descripcion_categoria = models.CharField(max_length=100)


    def __str__(self):
        return str(self.id_categoria)


class Miembro(models.Model):
    id_miembro = models.CharField(max_length=10, primary_key=True)
    nombre_miembro = models.CharField(max_length=100)
    ocupacion_cargo_miembro = models.CharField(max_length=100)
    info_miembro = models.TextField()
    foto_miembro = models.ImageField(
        upload_to='miembros/', 
        blank=True, 
        null=True)
    correo_miembro = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id_miembro)

class Ciudad(models.Model):
    id_ciudad = models.CharField(max_length=10, primary_key=True)
    nombre_ciudad = models.CharField(max_length=100)
    id_pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_ciudad)


class Iniciativa(models.Model):
    id_iniciativa = models.CharField(max_length=10, primary_key=True)
    nombre_iniciativa = models.CharField(max_length=100)
    descripcion_iniciativa = models.TextField()
    mision_iniciativa = models.TextField()
    vision_iniciativa = models.TextField()
    fecha_inicio_iniciativa = models.DateField()
    universidad_origen_iniciativa = models.CharField(max_length=100)
    numero_miembros_iniciativa = models.IntegerField()
    logo_iniciativa = models.ImageField(
        upload_to='logos_iniciativas/', 
        blank=True, 
        null=True)
    sitio_web_iniciativa = models.CharField(max_length=200)
    email_contacto_iniciativa = models.EmailField()
    id_categoria = models.ForeignKey(CategoriaIniciativa, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_iniciativa)

class Evento(models.Model):
    id_evento = models.CharField(max_length=10, primary_key=True)
    nombre_evento = models.CharField(max_length=100)
    descripcion_evento = models.TextField()
    fecha_inicio_evento = models.DateTimeField()
    fecha_fin_evento = models.DateTimeField()
    id_ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_evento)

class Sede(models.Model):
    id_sede = models.CharField(max_length=10, primary_key=True)
    nombre_sede = models.CharField(max_length=100)
    link_maps_sede = models.CharField(max_length=100)
    telefono_sede = models.CharField(max_length=100)
    direccion_ubicacion = models.CharField(max_length=100)
    id_iniciativa = models.ForeignKey(Iniciativa, on_delete=models.CASCADE)
    id_ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_sede)


class RedSocial(models.Model):
    id_red_social = models.CharField(max_length=10, primary_key=True)
    plataforma_red_social = models.CharField(max_length=20)
    url_red_social = models.CharField(max_length=200)
    id_iniciativa = models.ForeignKey(Iniciativa, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_red_social)

#Esto es lo míooo
class GaleriaEvento(models.Model):
    id_galeria = models.CharField(max_length=10, primary_key=True)
    imagen_galeria = models.ImageField(
        upload_to='galeria/', 
        blank=True, 
        null=True)
    descripcion_galeria = models.CharField(max_length=100)
    id_evento = models.ForeignKey(Evento, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_galeria)


class MiembroIniciativa(models.Model):
    id_miembro_iniciativa = models.CharField(max_length=10, primary_key=True)
    id_miembro = models.ForeignKey(Miembro, on_delete=models.CASCADE)
    id_iniciativa = models.ForeignKey(Iniciativa, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_miembro_iniciativa)


class IniciativaEvento(models.Model):
    id_iniciativa_evento = models.CharField(max_length=10, primary_key=True)
    id_iniciativa = models.ForeignKey(Iniciativa, on_delete=models.CASCADE)
    id_evento = models.ForeignKey(Evento, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_iniciativa_evento)


class MiembroEvento(models.Model):
    id_miembro_evento = models.CharField(max_length=10, primary_key=True)
    id_miembro = models.ForeignKey(Miembro, on_delete=models.CASCADE)
    id_evento = models.ForeignKey(Evento, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_miembro_evento)