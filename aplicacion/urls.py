
from django.conf.urls import url
from .views import crearGrado
urlpatterns =[
url(r'^crear_grado/',crearGrado, name ="CreaGrado"),
]
