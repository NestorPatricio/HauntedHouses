from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.conf import settings


class CustomAccountManager(BaseUserManager):
    
    def create_user(self, rut, email, password, **other_fields):
        if not rut:
            raise ValueError('Debes ingresar un RUT.')
        
        email = self.normalize_email(email)
        user = self.model(rut = rut, email = email, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, rut, email, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        return self.create_user(rut, email, password, **other_fields)


class TipoUser(models.Model):
    user_type = models.CharField(max_length = 20, null = False, blank = False)

    def __str__(self):
        return str(self.user_type)


class TipoInmueble(models.Model):
    property_type = models.CharField(max_length = 15, null = False, blank = False)

    def __str__(self):
        return str(self.property_type)


class Comuna(models.Model):
    municipality = models.CharField(max_length = 50)

    def __str__(self):
        return str(self.municipality)


class Region(models.Model):
    region = models.CharField(max_length = 50)

    def __str__(self):
        return str(self.region)


# Conversado con el relator Carlos García:
# Solicito realizar el modelo Profile usando 'AbstractBaseUser' como superclase, para practicar.
# Soy consciente de que no es la forma más fácil y que deberé de adaptar algunos comandos a como lo tienen mis compañeros.
class Profile(AbstractBaseUser, PermissionsMixin):
    rut = models.CharField(max_length=10, unique = True)
    first_name = models.CharField(max_length = 50, null = False, blank = False)
    last_name = models.CharField(max_length = 50, null = False, blank = False)
    adress = models.CharField(max_length = 100, null = False, blank = False)
    phone_number = models.CharField(max_length = 9, null = False, blank = False)
    email = models.EmailField(max_length = 50, null = False, blank = False, unique = False)
    picture = models.URLField(null = False, blank = True)
    tipo_user = models.ForeignKey(
        'm7_python.TipoUser',
        on_delete = models.CASCADE,
        null = True, blank = True)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'rut'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return f'Usuario RUT {self.rut}'


class Inmueble(models.Model):
    name = models.CharField(max_length = 100, default = '')
    description = models.TextField(null = False, blank = False)
    builded_sqm = models.IntegerField(null = False, blank = False)
    terrain_sqm = models.IntegerField(null = False, blank = False)
    parkings = models.IntegerField(default = 0)
    rooms = models.IntegerField(default = 0)
    bathrooms = models.IntegerField(default = 0)
    adress = models.CharField(max_length = 100, null = False, blank = False)
    rent_price = models.FloatField(null = False, blank = False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
        null = True, blank = True)
    tipo_inmueble = models.ForeignKey('m7_python.TipoInmueble',
        on_delete = models.CASCADE,
        null = True, blank = True)
    comuna = models.ForeignKey('m7_python.Comuna',
        on_delete = models.CASCADE,
        null = True, blank = True)
    region = models.ForeignKey('m7_python.Region',
        on_delete = models.CASCADE,
        null = True, blank = True)

    def __str__(self):
        return f'Propiedad número {self.id}'
