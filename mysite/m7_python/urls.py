from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import index, register, complement, users_intro, profile, add_property

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
    path('update/', profile, name = 'actualizarse'),
    # example: /add_new/
    path('add_new/', add_property, name = 'agrégala'),
]
