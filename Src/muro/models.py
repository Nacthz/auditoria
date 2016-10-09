from django.db import models
from evaluacion.models import *
from django.contrib.auth.models import User

class Trabajo(models.Model):
	empresa = models.ForeignKey(User, related_name='usuario_empresa', on_delete=models.CASCADE)
	auditor = models.ForeignKey(User, related_name='usuario_auditor', null=True, blank=True, on_delete=models.CASCADE)
	evaluacion = models.ForeignKey(Evaluacion, related_name='evaluacion', null=True, blank=True)
	preparacion = models.ForeignKey(Evaluacion, related_name='preparacion', null=True, blank=True)
	creacion = models.DateTimeField(auto_now_add=True)
	inicio = models.DateTimeField(null=True, blank=True)
	estado = models.ForeignKey('Estado')

	def __str__(self):
		return self.empresa.first_name + ' - ' + self.evaluacion.getNombre() + ' - ' + self.evaluacion.getFecha()

	def getNombreEmpresa(self):
		return self.empresa.first_name

	def getNombreAuditor(self):
		if(self.auditor == None):
			return 'En espera...';
		return self.auditor.first_name

	def getNombreCertificacion(self):
		return self.evaluacion.getNombre()

	def getFecha(self):
		return formats.date_format(self.creacion, "SHORT_DATETIME_FORMAT")

	def getActual(self):
		if self.estado.titulo == 'Activo':
			return self.preparacion.certificacion
		else:
			return self.evaluacion.certificacion

	def isActive(self):
		respuesta = False
		if self.estado.titulo == 'Activo':
			respuesta = True
		return respuesta

	def isAnexo(self):
		respuesta = False
		if self.estado.titulo == 'Anexo':
			respuesta = True
		return respuesta

	def getUrl(self):
		return reverse("muro:ver", kwargs={"id": self.id})

	def getUrlAnexo(self):
		return reverse("evaluacion:ver", kwargs={"id": self.id, "formulario": self.evaluacion.id})

	def getUrlPreparacion(self):
		return reverse("evaluacion:ver", kwargs={"id": self.id, "formulario": self.preparacion.id})

	def getUrlTomar(self):
		return reverse("muro:tomar", kwargs={"id": self.id})


class Estado(models.Model):
	titulo = models.CharField(max_length=120, unique=True)

	def __str__(self):
		return self.titulo