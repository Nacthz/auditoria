from django.contrib import admin
import nested_admin
from .models import *

class CalificacionInline(nested_admin.NestedTabularInline):
	model = Calificacion
	extra = 0

class EvaluacionAdmin(nested_admin.NestedModelAdmin):
	list_display = ['certificacion', 'get_fecha']

	inlines = [
		CalificacionInline,
	]

	def get_fecha(self, obj):
		return obj.getFecha()
	get_fecha.short_description = 'Fecha'
	get_fecha.admin_order_field = 'creacion'

	class Meta:
		model = Evaluacion

admin.site.register(Evaluacion, EvaluacionAdmin)
admin.site.register(Calificacion)
