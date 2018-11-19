from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Materia, MateriaAdmin)
admin.site.register(Grado, GradoAdmin)
admin.site.register(Pemsum)
