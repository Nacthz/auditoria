from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^perfil/',  include('usuario.urls', namespace="usuario")),
    url(r'^nested_admin/', include('nested_admin.urls')),
]
