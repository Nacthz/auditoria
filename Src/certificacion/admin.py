from django.contrib import admin
import nested_admin
from .models import *

class ControlInline(nested_admin.NestedTabularInline):
	model = Control
	extra = 0

class ObjetivoInline(nested_admin.NestedTabularInline):
	model = Objetivo
	extra = 0
	inlines = [
		ControlInline,
	]

class DominioInline(nested_admin.NestedTabularInline):
	model = Dominio
	extra = 0
	inlines = [
		ObjetivoInline,
	]

class CertificacionAdmin(nested_admin.NestedModelAdmin):
	list_display = ["nombre"]
	inlines = [
		DominioInline,
	]
	class Meta:
		model = Certificacion

admin.site.register(Certificacion, CertificacionAdmin)
admin.site.register(Dominio)
admin.site.register(Objetivo)
admin.site.register(Control)