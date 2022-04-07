from django.contrib import admin

from m7_python.models import Comuna, Region, TipoInmueble, Inmueble, TipoUser, Profile

admin.site.register(Comuna)
admin.site.register(Region)
admin.site.register(TipoInmueble)
admin.site.register(Inmueble)
admin.site.register(Profile)
admin.site.register(TipoUser)

""" Info del otro poryecto:

from django.contrib.auth.admin import UserAdmin

from rent_page.models import CustomUser, Property, Request, Contract


class UserAdminConfig(UserAdmin):
    search_fields = ('rut', 'email', 'phone_number')
    list_display = ('rut', 'first_name', 'last_name', 'email', 'phone_number')
    ordering = ('rut',)
    
    fieldsets = (
        (None, {"fields": ('first_name', 'last_name', 'rut'),}),
        ('Contact', {'fields': ('email', 'phone_number', 'adress')}),
        ('Personal pic', {'fields': ('picture',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff')}),
    )

    add_fieldsets = (
        (None, {'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'rut', 'password1', 'password2'),}),
        ('Contact', {'classes': ('wide',),
            'fields': ('email', 'phone_number', 'adress')}),
        ('Personal pic', {'classes': ('wide',),
            'fields': ('picture',)}),
        ('Permissions', {'classes': ('wide',),
            'fields': ('is_active', 'is_staff')}),
    )
"""