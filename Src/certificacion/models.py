from django.db import models

class Certifiacion(models.Model):
	nombre = models.CharField(max_length=300)

	def __str__(self):
		return self.nombre

class Dominio(models.Model):
	nombre = models.CharField(max_length=300)
	numero = models.CharField(max_length=30, default='')
	certifiacion = models.ForeignKey(Certifiacion)

	def __str__(self):
		return self.nombre

class Objetivo(models.Model):
	nombre = models.CharField(max_length=300)
	numero = models.CharField(max_length=30, default='')
	domino = models.ForeignKey(Dominio)

	def __str__(self):
		return self.nombre

class Control(models.Model):
	nombre = models.CharField(max_length=1000)
	numero = models.CharField(max_length=30, default='')
	objetivo = models.ForeignKey(Objetivo)

	def __str__(self):
		return self.nombre
