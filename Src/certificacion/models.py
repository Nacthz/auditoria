from django.db import models

class Certificacion(models.Model):
	nombre = models.CharField(max_length=300)

	def __str__(self):
		return self.nombre

class Dominio(models.Model):
	nombre = models.CharField(max_length=300)
	numero = models.CharField(max_length=30, default='')
	certificacion = models.ForeignKey(Certificacion)

	def __str__(self):
		return self.nombre

class Objetivo(models.Model):
	nombre = models.CharField(max_length=300)
	numero = models.CharField(max_length=30, default='')
	dominio = models.ForeignKey(Dominio)

	def __str__(self):
		return self.nombre

class Control(models.Model):
	nombre = models.CharField(max_length=1000)
	numero = models.CharField(max_length=30, default='')
	objetivo = models.ForeignKey(Objetivo)

	def __str__(self):
		return self.nombre
