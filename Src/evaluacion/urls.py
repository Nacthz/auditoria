from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^(?P<id>\d+)/(?P<formulario>\d+)/$', ver, name="ver"),
	url(r'^post/guardar/$', guardar_post, name="guardar_post"),
	url(r'^post/calificaciones/$', get_calificaciones, name="get_calificaciones"),
]
