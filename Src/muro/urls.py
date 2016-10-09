from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^lista/$', lista, name="lista"),
	url(r'^ver/(?P<id>\d+)/$', ver, name="ver"),
	url(r'^crear/$', crear, name="crear"),
	url(r'^descargar/(?P<id>\d+)/$', descargar, name="descargar"),
	url(r'^post/crear$', crear_post, name="crear_post"),
	url(r'^post/tomar/(?P<id>\d+)/$', tomar, name="tomar"),
]
