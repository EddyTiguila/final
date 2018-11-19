from django.db import models
from django.contrib import admin


class Materia(models.Model):
    id = models.AutoField(primary_key =True)
    nombre  =   models.CharField(max_length=30)
    creditos  =   models.CharField(max_length=30)
    def __str__(self):
        return self.nombre


class Grado(models.Model):
    id = models.AutoField(primary_key =True)
    nombre    = models.CharField(max_length=60)
    seccion    = models.CharField(max_length=60)
    incripcion  = models.IntegerField()
    materia   = models.ManyToManyField(Materia, through='Pemsum')
    def __str__(self):
        return self.nombre

class Pemsum(models.Model): 
    id = models.AutoField(primary_key =True)
    nombre    = models.CharField(max_length=60, null=True)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    grado = models.ForeignKey(Grado, on_delete=models.CASCADE)
    descripcion   = models.CharField(max_length=60, null=True)
    def __str__(self):
        return self.materia

class PemsumInLine(admin.TabularInline):
    model=Pemsum
    extra=1

class MateriaAdmin(admin.ModelAdmin):
    inlines = (PemsumInLine,)

class GradoAdmin(admin.ModelAdmin):
    inlines=(PemsumInLine,)


# Create your models here.
