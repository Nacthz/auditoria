from django.db import models
from certificacion.models import *

class Evaluacion(models.Model):
	creacion = models.DateTimeField(auto_now_add=True)
	actualizacion = models.DateTimeField(auto_now=True)

class Calificacion(models.Model):
	control = models.ForeignKey(Control)
	evaluacion = models.ForeignKey(Evaluacion)
	active = models.BooleanField(default=True)

	def __str__(self):
		return self.control.nombre
	