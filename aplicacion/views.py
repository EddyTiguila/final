from django.shortcuts import render, redirect
from .models import Grado
from .models import Materia
from .models import Pemsum
from .forms import GradoForm

from django.contrib import messages

def crearGrado(request):
    if request.method == "POST":

        formulario = GradoForm(request.POST)

        if formulario.is_valid():

            grado = Grado.objects.create(nombre=formulario.cleaned_data['nombre'],
            seccion = formulario.cleaned_data['seccion'], incripcion=formulario.cleaned_data['incripcion'])

            for materia_id in request.POST.getlist('materia'):

                pemsum = Pemsum (nombre='--',materia=materia, grado=grado, descripcion='--')

                pemsum.save()

            messages.add_message(request, messages.SUCCESS, 'Torneo Guardado Exitosamente')
            return redirect('listar_torneo')

    else:

        formulario = GradoForm()

    return render(request, 'aplicacion/crear_grado.html', {'formulario': formulario})

# Create your views here.
