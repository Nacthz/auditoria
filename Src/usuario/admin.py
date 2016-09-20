from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import *

class UsuarioInline(admin.StackedInline):
	model = Perfil
	can_delete = False
	verbose_name_plural = 'usuario'

class UserAdmin(UserAdmin):
	inlines = (UsuarioInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Tipo)