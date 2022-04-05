from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager


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


class CustomUser(AbstractBaseUser, PermissionsMixin):
    rut = models.CharField(max_length=10, unique = True)
    first_name = models.CharField(max_length = 50, null = False, blank = False)
    last_name = models.CharField(max_length = 50, null = False, blank = False)
    adress = models.CharField(max_length = 100, null = False, blank = False)
    phone_number = models.CharField(max_length = 9, null = False, blank = False)
    email = models.EmailField(max_length = 50, null = False, blank = False, unique = True)
    picture = models.URLField(default = 'Sin imagen disponible', null = False, blank = True)
    is_active = models.BooleanField(default = False)
    is_staff = models.BooleanField(default = False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'rut'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return f'Usuario RUT {self.rut}'


class Property(models.Model):
    PROPERTY_KIND = [
        ('CASA', 'Casa'),
        ('DPTO', 'Departamento'),
        ('PARC', 'Parcela'),
        (None, 'Sin información'),
    ]

    description = models.TextField(null = False, blank = False)
    builded_sqm = models.IntegerField(null = False, blank = False)
    total_sqm = models.IntegerField(null = False, blank = False)
    parkings = models.IntegerField(default = 0)
    rooms = models.IntegerField(default = 0)
    bathrooms = models.IntegerField(default = 0)
    adress = models.CharField(max_length = 100, null = False, blank = False)
    municipality = models.CharField(max_length = 30, null = False, blank = False)
    rent_price = models.FloatField(null = False, blank = False)
    property_kind = models.CharField(max_length = 4, choices = PROPERTY_KIND, null = False, blank = False)
    users = models.ManyToManyField(CustomUser, through = 'Contract', related_name = 'properties')

    def __str__(self):
        return f'Propiedad número {self.id}'


class Contract(models.Model):
    USER_KIND = [
        ('arrendatar', 'Arrendatario'),
        ('arrendador', 'Arrendador'),
        (None, 'Sin información')
    ]

    user_rut = models.ForeignKey(CustomUser, verbose_name = "rut del usuario", on_delete=models.CASCADE)
    property_id = models.ForeignKey(Property, verbose_name = "id de la propiedad", on_delete = models.CASCADE)
    user_kind = models.CharField(max_length = 10, choices = USER_KIND, null = False, blank = False)


class Request(models.Model):
    user_rut = models.ForeignKey(CustomUser, verbose_name = "rut del usuario", on_delete=models.CASCADE)
    property_id = models.ForeignKey(Property, verbose_name = "id de la propiedad", on_delete = models.CASCADE)
    ask = models.TextField(null = False, blank = False)