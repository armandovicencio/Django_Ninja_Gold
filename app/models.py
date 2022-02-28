from django.db import models

# Create your models here.
class Ciudad(models.Model):
    nombre = models.CharField(max_length=50)
    cantidad_habitantes = models.IntegerField(default=10, unique=True)
    temperatura = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} C.H.:{self.cantidad_habitantes} MM"

class Region(models.Model):
    nombre = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Movie(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField()
    release_date = models.DateTimeField()
    duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Camion(models.Model):

    SIZE_CHICO = 'C'
    SIZE_MEDIANO = 'M'
    SIZE_GRANDE = 'G'

    TIPO_CAMION = (
        (SIZE_CHICO, 'CHICO'),
        (SIZE_MEDIANO, 'MEDIANO'),
        (SIZE_GRANDE, 'GRANDE'),
    )

    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=1, choices=TIPO_CAMION, default=SIZE_CHICO)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # rutas = Lista de rutas del camion 
    # choferes = Lista de Choferes asociados al camion
    def __str__(self):
        return f"{self.nombre} - {self.tipo}"
    
class Ruta(models.Model):
    camion = models.ForeignKey(Camion, related_name="rutas", on_delete=models.CASCADE)
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} - {self.origen} - {self.destino}"


class Chofer(models.Model):
    camiones = models.ManyToManyField(Camion, related_name="choferes")
    nombre = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre}"