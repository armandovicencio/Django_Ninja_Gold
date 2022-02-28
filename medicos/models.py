from django.db import models

# Create your models here.
class Medico(models.Model):

    ESPECIALIDAD_CHOICES = (
        ('A', 'Cardiologia'),
        ('B', 'Oftalmologia'),
        ('C', 'Pediatria'),
        ('D', 'Ginecologia'),
        ('E', 'Otorrinolaringologia'),
        ('F', 'Neurologia'),
        ('G', 'Urologia'),
        ('H', 'Traumatologia'),
        ('I', 'Odontologia'),
    )

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=1, choices=ESPECIALIDAD_CHOICES, default='A')
    telefono = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    def __str__(self):
        return self.nombre + ' ' + self.apellido
    
