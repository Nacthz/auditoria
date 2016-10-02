from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^perfil/', include('usuario.urls', namespace="usuario")),
    url(r'^evaluacion/', include('evaluacion.urls', namespace="evaluacion")),
    url(r'^muro/', include('muro.urls', namespace="muro")),
    url(r'^nested_admin/', include('nested_admin.urls')),
    url(r'^', include('raiz.urls', namespace="raiz")),
]
