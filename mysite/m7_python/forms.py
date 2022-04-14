from django import forms
from django.contrib.auth.forms import UserCreationForm

from m7_python.models import Profile


class UserForm(UserCreationForm):
    rut = forms.CharField(max_length = 10, label = 'RUT')
    email = forms.EmailField(max_length = 50, label = 'Correo electrónico')
    password1 = forms.CharField(label = 'Contraseña', widget = forms.PasswordInput)
    password2 = forms.CharField(label = 'Reingresa tu contraseña', widget = forms.PasswordInput)

    class Meta:
        model = Profile
        fields = ('rut', 'email', 'password1', 'password2')
        #help_text = {k:"" for k in fields }


class CompletingUserForm(forms.Form):
    type_users = (
        (1, 'Arrendatario'),
        (2, 'Arrendador'),
    )
    first_name = forms.CharField(max_length = 50, label = 'Nombres')
    last_name = forms.CharField(max_length = 50, label = 'Apellidos')
    type_user = forms.ChoiceField(choices = type_users, label = 'Tipo de usuario')
    adress = forms.CharField(max_length = 100, label = 'Dirección')
    phone_number = forms.CharField(max_length = 9, label = 'Teléfono de contacto')
    picture = forms.URLField(required = False, label = 'Foto personal')


class UserUpdateForm(forms.ModelForm):
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
            'picture': "Fotografía",
        }