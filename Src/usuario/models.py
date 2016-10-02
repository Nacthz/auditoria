from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
	usuario = models.OneToOneField(User)
	tipo = models.ForeignKey('Tipo', null=True, blank=True)

	def __str__(self):
		return self.tipo.titulo

	def getTipo(self):
		return self.tipo.titulo

class Tipo(models.Model):
	titulo = models.CharField(max_length=120, unique=True)

	def __str__(self):
		return self.titulo