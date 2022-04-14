from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from m7_python.models import Profile, TipoUser
from m7_python.forms import UserForm, CompletingUserForm, UserUpdateForm

def index(request):
    return render(request, './m7_python/index.html', {})

@login_required
def users_intro(request):
    return render(request, './m7_python/dashboard.html', {})

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
            return HttpResponseRedirect('/login')
    else:
        form = CompletingUserForm()
    return render(request, './registration/complement.html', {'formulario': form})

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/dashboard')
    else:
        # 'instance=' permite que los campos no estén vacíos al momento de actualizar.
        form = UserUpdateForm(instance = request.user)
    return render(request, './m7_python/update_profile.html', {'formulario': form})