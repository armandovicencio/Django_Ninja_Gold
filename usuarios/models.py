from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])([A-Za-z\d$@$!%*?&]|[^ ]){8,15}$')



class UsuarioManager(models.Manager):

   
    
    def saludar(self, name=None):
        if name:
            print("HOLA A TI", name)
        return self


    def basic_validator(self, postData):


        errors = {}
        # agregue claves y valores al diccionario de errores para cada campo no válido
        if len(postData['nombre']) < 3:
            errors["nombre"] = "Nombre debe tener al menos 3 caraceteres"
        if len(postData['apellido']) < 5:
            errors["apellido"] = "apeliido no puede tener menos de 5 caracteres"

        if self.filter(email=postData['email']).exists():
            errors["email"] = "email existe."

        if postData['password']!= postData['confirmar_password']:
            errors["password"] = "las contraseñas no coinciden"

        if not PASSWORD_REGEX.match(postData['password']):
            errors["password2"] = "la contraseña no es segura. "

        return errors


# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    username = models.CharField(max_length=20, unique=True, verbose_name="Nombre de Usuario")
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=72)
    description = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UsuarioManager()

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"