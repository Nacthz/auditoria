import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from .models import *
from muro.models import Trabajo, Estado
from evaluacion.models import Calificacion
from certificacion.models import Control

def ver(request, id):
	trabajo = Trabajo.objects.get(id=id)

	datos = {
		'trabajo': trabajo,
		'estados': Estado.objects.all(),
		'usuario': request.user.perfil.getTipo()
	}
	return render(request, 'evaluacion.html', datos)

def get_calificaciones(request):
	trabajo = Trabajo.objects.get(id=request.POST['id'])
	calificaciones = Calificacion.objects.filter(evaluacion=trabajo.evaluacion)

	calificaciones_lista = {}

	i = 0
	for calificacion in calificaciones:
		calificaciones_lista[i] = {
			'control_id': calificacion.control.id,
			'comentario': calificacion.comentario,
			'estado': calificacion.cumplimiento
		}
		i+=1

	respuesta = {
		'calificaciones': calificaciones_lista
	}
	return HttpResponse(json.dumps(respuesta), content_type='application/json')

def guardar_post(request):
	controles = request.POST.getlist('controles[]')
	comentarios = request.POST.getlist('comentarios[]')
	comentarios_id = request.POST.getlist('comentarios_id[]')
	trabajo = Trabajo.objects.get(id=request.POST['trabajo'])
	evaluacion = trabajo.evaluacion

	trabajo.estado = Estado.objects.get(id=request.POST['estado'])
	trabajo.save()

	evaluacion.calificacion_set.all().update(cumplimiento=False, comentario='')

	for control_id in controles:
		control = Control.objects.get(id=control_id)
		Calificacion.objects.filter(evaluacion=evaluacion, control=control).update(cumplimiento=True)

	i = 0
	for comentario in comentarios:
		control = Control.objects.get(id=comentarios_id[i])
		Calificacion.objects.filter(evaluacion=evaluacion, control=control).update(comentario=comentario)
		i+=1

	return redirect('usuario:ingresar')