from django.contrib import admin
import nested_admin
from .models import *

class TrabajoAdmin(nested_admin.NestedModelAdmin):
	list_display = ['get_empresa', 'get_certificacion', 'get_fecha', 'get_auditor']

	def get_empresa(self, obj):
		return obj.empresa.first_name
	get_empresa.short_description = 'Empresa'
	get_empresa.admin_order_field = 'empresa__first_name'

	def get_certificacion(self, obj):
		return obj.evaluacion.getNombre()
	get_certificacion.short_description = 'Certificacion'
	get_certificacion.admin_order_field = 'evalucacion__certificacion'

	def get_fecha(self, obj):
		return obj.evaluacion.getFecha()
	get_fecha.short_description = 'Fecha'
	get_fecha.admin_order_field = 'evaluacion__creacion'

	def get_auditor(self, obj):
		auditor = obj.auditor
		return auditor.first_name + ' ' + auditor.last_name
	get_auditor.short_description = 'Auditor'
	get_auditor.admin_order_field = 'auditor__first_name'

	class Meta:
		model = Trabajo

admin.site.register(Trabajo, TrabajoAdmin)
admin.site.register(Estado)
