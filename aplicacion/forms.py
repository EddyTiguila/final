from django import forms
from .models import *

class PemsumForm(forms.ModelForm):
    class Meta:
        model= Pemsum
        fields =['nombre', 'materia', 'grado','descripcion',]

class MateriaForm(forms.ModelForm):
    class Meta:
        model= Materia
        fields =['nombre', 'creditos',]


class GradoForm(forms.ModelForm):
    class Meta:
        model= Grado
        fields =['nombre', 'seccion', 'incripcion','materia']
        def __init__ (self, *args, **kwargs):
            super(TorneoForm, self).__init__(*args, **kwargs)

#En este caso vamos a usar el widget checkbox multiseleccionable.

            self.fields["materia"].widget = forms.widgets.CheckboxSelectMultiple()

#Podemos usar un texto de ayuda en el widget

            self.fields["materia"].help_text = "Ingrese las materias"

#En este caso le indicamos que nos muestre todos los actores, pero aquí podríamos filtrar datos si fuera necesario

            self.fields["materia"].queryset = Equipo.objects.all()
