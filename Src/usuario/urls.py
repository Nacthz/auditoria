from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^$', index, name="inicio"),
	url(r'^ingresar/$', ingresar, name="ingresar"),
	url(r'^post/ingresar$', ingresar_post, name="ingresar_post"),
	url(r'^post/salir$', salir_post, name="salir_post"),
]
