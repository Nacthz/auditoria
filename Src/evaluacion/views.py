import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from .models import *
from muro.models import Trabajo, Estado
from evaluacion.models import Evaluacion, Calificacion, Cumplimiento
from certificacion.models import Control

def ver(request, id, formulario):
	usuario = request.user
	if not usuario.is_authenticated():
		return redirect('raiz:inicio')
		
	trabajo = Trabajo.objects.get(id=id)
	formulario = Evaluacion.objects.get(id=formulario)

	datos = {
		'trabajo': trabajo,
		'estados': Estado.objects.all(),
		'usuario': request.user.perfil.getTipo(),
		'formulario' : formulario
	}
	return render(request, 'evaluacion.html', datos)

def get_calificaciones(request):
	evaluacion = Evaluacion.objects.get(id=request.POST['evaluacion'])
	calificaciones = Calificacion.objects.filter(evaluacion=evaluacion)

	calificaciones_lista = {}

	i = 0
	for calificacion in calificaciones:
		calificaciones_lista[i] = {
			'control_id': calificacion.control.id,
			'comentario': calificacion.comentario,
			'cumplimiento': calificacion.cumplimiento.id
		}
		i+=1

	respuesta = {
		'calificaciones': calificaciones_lista
	}
	return HttpResponse(json.dumps(respuesta), content_type='application/json')


def guardar_post(request):
	if request.method == 'POST':
		data = request.POST
		evaluacion = Evaluacion.objects.get(id=request.POST['evaluacion'])

		trabajo = Trabajo.objects.get(id=data.get('trabajo'))
		trabajo.estado = Estado.objects.get(id=data.get('estado'))
		trabajo.save()

		preguntas = evaluacion.calificacion_set.all()
		for pregunta in preguntas:
			control_id = str(pregunta.control.id)

			comentario = data.get('json_data['+ control_id +'][comentario]')
			valoracion = data.get('json_data['+ control_id +'][valoracion]')

			cumplimiento = Cumplimiento.objects.get(id=valoracion)

			Calificacion.objects.filter(evaluacion=evaluacion, control_id=control_id).update(comentario=comentario, cumplimiento=cumplimiento)

	return redirect('muro:ver', id=trabajo.id)