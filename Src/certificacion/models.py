from django.db import models

class Certifiacion(models.Model):
	nombre = models.CharField(max_length=300)

	def __str__(self):
		return self.nombre

class Dominio(models.Model):
	nombre = models.CharField(max_length=300)
	numero = models.IntegerField(null=True, blank=True)
	certifiacion = models.ForeignKey(Certifiacion)

	def __str__(self):
		return self.nombre

class Objetivo(models.Model):
	nombre = models.CharField(max_length=300)
	numero = models.IntegerField(null=True, blank=True)
	domino = models.ForeignKey(Dominio)

	def __str__(self):
		return self.nombre

class Control(models.Model):
	nombre = models.CharField(max_length=1000)
	numero = models.IntegerField(null=True, blank=True)
	objetivo = models.ForeignKey(Objetivo)

	def __str__(self):
		return self.nombre
