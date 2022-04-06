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


class TipoInmueble(models.Model):
    property_type = models.CharField(max_length = 15, null = False, blank = False)


class Comuna(models.Model):
    municipality = models.CharField(max_length = 50)


class Region(models.Model):
    region = models.CharField(max_length = 50)


class Profile(AbstractBaseUser, PermissionsMixin):
    rut = models.CharField(max_length=10, unique = True)
    first_name = models.CharField(max_length = 50, null = False, blank = False)
    last_name = models.CharField(max_length = 50, null = False, blank = False)
    adress = models.CharField(max_length = 100, null = False, blank = False)
    phone_number = models.CharField(max_length = 9, null = False, blank = False)
    email = models.EmailField(max_length = 50, null = False, blank = False, unique = False)
    picture = models.URLField(default = 'Sin imagen disponible')
    tipo_user = models.OneToOneField(
        'm7_python.TipoUser',
        on_delete = models.CASCADE,
        null = False, blank = False,
        related_name = 'profile')
    is_active = models.BooleanField(default = False)
    is_staff = models.BooleanField(default = False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'rut'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return f'Usuario RUT {self.rut}'


class Inmueble(models.Model):
    description = models.TextField(null = False, blank = False)
    builded_sqm = models.IntegerField(null = False, blank = False)
    terrain_sqm = models.IntegerField(null = False, blank = False)
    parkings = models.IntegerField(default = 0)
    rooms = models.IntegerField(default = 0)
    bathrooms = models.IntegerField(default = 0)
    adress = models.CharField(max_length = 100, null = False, blank = False)
    rent_price = models.FloatField(null = False, blank = False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
        related_name = 'inmuebles',
        on_delete = models.CASCADE,
        null = True, blank = True)
    tipo_inmueble = models.ForeignKey('m7_python.TipoInmueble',
        related_name = 'inmuebles',
        on_delete = models.CASCADE,
        null = True, blank = True)
    comuna = models.ForeignKey('m7_python.Comuna',
        related_name = 'inmuebles',
        on_delete = models.CASCADE,
        null = True, blank = True)
    region = models.ForeignKey('m7_python.Region',
        related_name = 'inmuebles',
        on_delete = models.CASCADE,
        null = True, blank = True)

    def __str__(self):
        return f'Propiedad número {self.id}'