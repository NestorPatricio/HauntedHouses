from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import index, register, complement, users_intro, profile_update, add_property, property_update, property_delete

app_name = 'm7_python'

urlpatterns = [
    # example: /
    path('', index, name = 'principal'),
    # example: /dashboard/
    path('dashboard/', users_intro, name = 'panel'),
    # example: /login/
    path('login/', LoginView.as_view(next_page = 'm7_python:panel'), name = 'iniciar'),
    # example: /logout/
    path('logout/', LogoutView.as_view(next_page = 'm7_python:principal'), name = 'cerrar'),
    # example: /register/
    path('register/', register, name = 'registrarse'),
    # example: /complement/
    path('complement/', complement, name = 'complemento'),
    # example: /update/
    path('update/', profile_update, name = 'actualizarse'),
    # example: /add_new/
    path('add_new/', add_property, name = 'agrégala'),
    # example: /update_prop/
    path('update_prop/', property_update, name = 'actualízalo'),
    # example: /delete_prop/
    path('delete_prop/', property_delete, name = 'elimínala'),
]
