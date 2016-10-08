from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation

class Certificacion(models.Model):
	nombre = models.CharField(max_length=300, null=True, blank=True)
	tipo = models.ForeignKey('Tipo')
	preparacion = models.ForeignKey('self', null=True, blank=True)

	def __str__(self):
		return self.nombre

class Dominio(models.Model):
	nombre = models.CharField(max_length=300, null=True, blank=True)
	numero = models.CharField(max_length=30, null=True, blank=True)
	certificacion = models.ForeignKey('Certificacion')

	def __str__(self):
		return self.nombre

class Objetivo(models.Model):
	nombre = models.CharField(max_length=300, null=True, blank=True)
	numero = models.CharField(max_length=30, null=True, blank=True)
	dominio = models.ForeignKey('Dominio')

	def __str__(self):
		return self.nombre

class Control(models.Model):
	nombre = models.CharField(max_length=1000, null=True, blank=True)
	numero = models.CharField(max_length=30, null=True, blank=True)
	objetivo = models.ForeignKey('Objetivo')

	def __str__(self):
		return self.nombre

class Tipo(models.Model):
	titulo = models.CharField(max_length=120, unique=True, null=True, blank=True)

	def __str__(self):
		return self.titulo