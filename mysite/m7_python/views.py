from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from m7_python.models import Profile, TipoUser, Inmueble, TipoInmueble, Comuna, Region
from m7_python.forms import UserForm, CompletingUserForm, UserUpdateForm, InmuebleForm, InmuebleUpdateForm

def index(request):
    return render(request, './m7_python/index.html', {})

@login_required
def users_intro(request):
    usuario = request.user
    sapo = True
    if usuario.tipo_user_id == 1:
        inmuebles = Inmueble.objects.filter(user = usuario)
    else:
        inmuebles = Inmueble.objects.all()
    if len(inmuebles) == 0:
        sapo = False
    return render(request, './m7_python/dashboard.html', {'properties': inmuebles, 'checker': sapo})

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            # Una vez creado el usuario exitosamente, se le envía a completar el registro.
            return HttpResponseRedirect(
                '/complement?user=' + str(form.cleaned_data['rut'])
                )
    else:
        form = UserForm()
    return render(request, './registration/register.html', {'formulario': form})

def complement(request):
    rut = request.GET['user']
    if request.method == 'POST':
        form = CompletingUserForm(request.POST)
        if form.is_valid():
            # Se extraen los datos del 'request' para actualizar la información del usuario.
            user = Profile.objects.get(rut = rut)
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.tipo_user = TipoUser.objects.get(pk = int(form.cleaned_data['type_user']))
            user.adress = form.cleaned_data['adress']
            user.phone_number = form.cleaned_data['phone_number']
            user.picture = form.cleaned_data['picture']
            user.save()
            messages.success(request, f'El usuario {user.first_name} ha sido creado exitosamente.')
            return HttpResponseRedirect('/login')
    else:
        form = CompletingUserForm()
    return render(request, './registration/complement.html', {'formulario': form})

@login_required
def profile_update(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Los datos del usuario{form.cleaned_data["first_name"]} han sido actualizados exitosamente.')
            return HttpResponseRedirect('/dashboard')
    else:
        # 'instance=' permite que los campos no estén vacíos al momento de actualizar.
        form = UserUpdateForm(instance = request.user)
    return render(request, './registration/update_profile.html', {'formulario': form})

@login_required
def add_property(request):
    if request.method == 'POST':
        form = InmuebleForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            builded_sqm = form.cleaned_data['builded_sqm']
            terrain_sqm = form.cleaned_data['terrain_sqm']
            parkings = form.cleaned_data['parkings']
            rooms = form.cleaned_data['rooms']
            bathrooms = form.cleaned_data['bathrooms']
            adress = form.cleaned_data['adress']
            rent_price = form.cleaned_data['rent_price']
            tipo_inmueble = TipoInmueble.objects.get(pk = int(form.cleaned_data['tipo_inmueble']))
            comuna = Comuna.objects.get(pk = int(form.cleaned_data['comuna']))
            region = Region.objects.get(pk = int(form.cleaned_data['region']))

            Inmueble.objects.create(
                user = user,
                name = name,
                description = description,
                builded_sqm = builded_sqm,
                terrain_sqm = terrain_sqm,
                parkings = parkings,
                rooms = rooms,
                bathrooms = bathrooms,
                adress = adress,
                rent_price = rent_price,
                tipo_inmueble = tipo_inmueble,
                comuna = comuna,
                region = region,
            )
            messages.success(request, 'El inmueble ha sido agregado exitosamente.')
            return HttpResponseRedirect('/dashboard')
    else:
        form = InmuebleForm()
    return render(request, './m7_python/add_property.html', {'formulario': form})

@login_required
def property_update(request):
    property = Inmueble.objects.get(id = request.GET['id'])
    if request.method == 'POST':
        form = InmuebleUpdateForm(request.POST, instance = property)
        if form.is_valid():
            form.save()
            messages.success(request, 'Los datos de su propiedad han sido actualizados exitosamente.')
            return HttpResponseRedirect('/dashboard')
    else:
        form = InmuebleUpdateForm(instance = property)
    return render(request, './registration/update_property.html', {'formulario': form, 'propiedad': property})

@login_required
def property_delete(request):
    property = Inmueble.objects.get(id = request.GET['id'])
    property.delete()
    messages.success(request, 'Los datos de su propiedad han sido eliminados.')
    return HttpResponseRedirect('/dashboard')