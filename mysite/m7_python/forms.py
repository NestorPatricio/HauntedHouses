from django import forms
from django.contrib.auth.forms import UserCreationForm

from m7_python.models import Profile, Comuna, Region, Inmueble


class UserForm(UserCreationForm):
    rut = forms.CharField(
        max_length = 10,
        label = 'RUT',
        widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Ex: 12345678-9'}))
    email = forms.EmailField(
        max_length = 50,
        label = 'Correo electrónico',
        widget = forms.EmailInput(attrs = {'class': 'form-control', 'placeholder': 'Ex: micorreo@electronico.com'}))
    password1 = forms.CharField(
        label = 'Contraseña',
        widget = forms.PasswordInput(attrs = {'class': 'form-control', 'placeholder': '8 caracteres mínimo'}))
    password2 = forms.CharField(
        label = 'Reingresa tu contraseña',
        widget = forms.PasswordInput(attrs = {'class': 'form-control', 'placeholder': '8 caracteres mínimo'}))

    class Meta(UserCreationForm.Meta):
        model = Profile
        fields = ('rut', 'email', 'password1', 'password2')


class CompletingUserForm(forms.Form):
    TYPE_USER = (
        (1, 'Arrendatario'),
        (2, 'Arrendador'))

    first_name = forms.CharField(
        max_length = 50,
        label = 'Nombres',
        widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Ex: Juanín Juanoso'}))
    last_name = forms.CharField(
        max_length = 50,
        label = 'Apellidos',
        widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Ex: Pérez Pereira'}))
    type_user = forms.CharField(
        label = 'Tipo de usuario',
        widget = forms.Select(attrs = {'class': 'form-control'}, choices = TYPE_USER))
    adress = forms.CharField(
        max_length = 100,
        label = 'Dirección',
        widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Calle, número, departamento, ciudad.'}))
    phone_number = forms.CharField(
        max_length = 9,
        label = 'Teléfono de contacto',
        widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Ex: 987654321'}))
    picture = forms.URLField(
        required = False,
        label = 'Foto personal',
        widget = forms.URLInput(attrs = {'class': 'form-control', 'placeholder': 'Ex: http://mi.foto.com'}))


class UserUpdateForm(forms.ModelForm):
    picture = forms.URLField(
        required = False,
        label = 'Foto personal',
        widget = forms.URLInput(attrs = {'class': 'form-control', 'placeholder': 'Ex: http://mi.foto.com'}))

    class Meta:
        model = Profile
        fields = (
            'first_name',
            'last_name',
            'email',
            'adress',
            'phone_number',
            'picture',
            )
        labels = {
            'first_name': "Nombres",
            'last_name': "Apellidos",
            'email': "Correo electrónico",
            'adress': "Dirección",
            'phone_number': "Teléfono de contacto",
        }
        widgets = {
            'first_name': forms.TextInput(attrs = {'class': 'form-control'}),
            'last_name': forms.TextInput(attrs = {'class': 'form-control'}),
            'email': forms.EmailInput(attrs = {'class': 'form-control'}),
            'adress': forms.TextInput(attrs = {'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs = {'class': 'form-control'}),
        }


class InmuebleForm(forms.Form):
    TYPE_PROPERTY = (
        (1, 'Casa'),
        (2, 'Departamento'),
        (3, 'Parcela'),
        (4, 'Estacionamiento'),
        (5, 'Otro'))
    MUNICIPALITY = [(comuna.id, comuna.municipality) for comuna in Comuna.objects.all().order_by('municipality')]
    REGION = [(region.id, region.region) for region in Region.objects.all()]

    name = forms.CharField(
        max_length = 100,
        label = 'Nombre de la publicación',
        widget = forms.TextInput(attrs = {
            'class': 'form-control',
            'placeholder': 'Un espeluznante y atractivo resumen en 100 caracteres.'}))
    description = forms.CharField(
        max_length = 500,
        label = 'Descripción de la propiedad',
        widget = forms.Textarea(attrs = {
            'class': 'form-control',
            'style': 'resize: none;',
            'rows': '6',
            'placeholder': 'Tu inmueble en 500 caracteres.'}))
    tipo_inmueble = forms.CharField(
        label = 'Tipo de inmueble',
        widget = forms.Select(attrs = {'class': 'form-control'}, choices = TYPE_PROPERTY))
    builded_sqm = forms.IntegerField(
        label = 'M2 construidos',
        min_value = 0,
        widget = forms.NumberInput(attrs = {'class': 'form-control'}))
    terrain_sqm = forms.IntegerField(
        label = 'M2 del terreno',
        min_value = 0,
        widget = forms.NumberInput(attrs = {'class': 'form-control'}))
    parkings = forms.IntegerField(
        label = 'Estacionamientos',
        min_value = 0,
        widget = forms.NumberInput(attrs = {'class': 'form-control'}))
    rooms = forms.IntegerField(
        label = 'Habitaciones',
        min_value = 0,
        widget = forms.NumberInput(attrs = {'class': 'form-control'}))
    bathrooms = forms.IntegerField(
        label = 'Baños',
        min_value = 0,
        widget = forms.NumberInput(attrs = {'class': 'form-control'}))
    rent_price = forms.FloatField(
        label = 'Precio del arriendo mensual',
        min_value = 0,
        widget = forms.NumberInput(attrs = {'class': 'form-control'}))
    adress = forms.CharField(
        max_length = 100,
        label = 'Dirección',
        widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Calle, número, departamento, otro.'}))
    region = forms.CharField(
        label = 'Región',
        widget = forms.Select(attrs = {'class': 'form-control'}, choices = REGION))
    comuna = forms.CharField(
        label = 'Comuna',
        widget = forms.Select(attrs = {'class': 'form-control'}, choices = MUNICIPALITY))


class InmuebleUpdateForm(forms.ModelForm):
    class Meta:
        model = Inmueble
        fields= (
            'name',
            'description',
            'builded_sqm',
            'terrain_sqm',
            'rooms',
            'bathrooms',
            'parkings',
            'rent_price',
        )
        labels = {
            'name': 'Nombre de la publicación',
            'description': 'Descripción de la propiedad',
            'builded_sqm': 'M2 construidos',
            'terrain_sqm': 'M2 del terreno',
            'rooms': 'Habitaciones',
            'bathrooms': 'Baños',
            'parkings': 'Estacionamientos',
            'rent_price': 'Precio del arriendo mensual',
        }
        widgets = {
            'name': forms.TextInput(attrs = {'class': 'form-control'}),
            'description': forms.Textarea(attrs = {
                'class': 'form-control',
                'style': 'resize: none;',
                'rows': '6'}),            
            'builded_sqm': forms.NumberInput(attrs = {'class': 'form-control'}),
            'terrain_sqm': forms.NumberInput(attrs = {'class': 'form-control'}),
            'rooms': forms.NumberInput(attrs = {'class': 'form-control'}),
            'bathrooms': forms.NumberInput(attrs = {'class': 'form-control'}),
            'parkings': forms.NumberInput(attrs = {'class': 'form-control'}),
            'rent_price': forms.NumberInput(attrs = {'class': 'form-control'}),
        }