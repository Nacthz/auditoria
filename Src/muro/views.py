from io import BytesIO as stringIOModule
import xlsxwriter
import time
from django.shortcuts import render, redirect
from muro.models import Trabajo, Estado
from certificacion.models import Certificacion, Control
from evaluacion.models import Evaluacion, Calificacion
from django.http import HttpResponse

#Funcion para tomar un trabajo
def tomar(request, id):
	usuario = request.user
	if not usuario.is_authenticated():
		return redirect('raiz:inicio')

	trabajo = Trabajo.objects.get(id=id)
	trabajo.auditor = usuario
	trabajo.estado = Estado.objects.get(titulo='Activo')
	trabajo.save() 

	return redirect('usuario:inicio')

#Vista para ver trabajos inactivos
def lista(request):
	usuario = request.user
	if not usuario.is_authenticated():
		return redirect('raiz:inicio')

	trabajos = Trabajo.objects.filter(estado__titulo='Inactivo').order_by('-creacion')
	datos = {
		'trabajos': trabajos,
	}

	return render(request, 'lista.html', datos)

#Vista para ver trabajo unico
def ver(request, id):
	usuario = request.user
	if not usuario.is_authenticated():
		return redirect('raiz:inicio')

	trabajo = Trabajo.objects.get(id=id)
	datos = {
		'trabajo': trabajo,
		'perfil': usuario.perfil.getTipo()
	}

	return render(request, 'trabajo.html', datos)

#Vista para crear trabajos
def crear(request):
	usuario = request.user
	perfil = usuario.perfil.getTipo()

	if not usuario.is_authenticated() or perfil != 'Empresa':
		return redirect('raiz:inicio')

	certificaciones = Certificacion.objects.filter(tipo__titulo='Anexo')

	datos = {
		'certificaciones': certificaciones,
	}

	return render(request, 'crear_trabajo.html', datos)

#Funcion para crear un trabajo
def crear_post(request):
	usuario = request.user
	if not usuario.is_authenticated():
		return redirect('raiz:inicio')

	certificacion = Certificacion.objects.get(id=request.POST['certificacion'])
	evaluacion = Evaluacion.objects.create(certificacion=certificacion)
	preparacion = Evaluacion.objects.create(certificacion=certificacion.preparacion)

	estado = Estado.objects.get(titulo='Inactivo')

	Trabajo.objects.create(empresa=usuario, evaluacion=evaluacion, preparacion=preparacion, estado=estado)

	#Evaluacion
	controles = Control.objects.filter(objetivo__dominio__certificacion=certificacion)
	for control in controles:
		Calificacion.objects.create(control=control, evaluacion=evaluacion)

	#Peparacion
	controles = Control.objects.filter(objetivo__dominio__certificacion=certificacion.preparacion)
	for control in controles:
		Calificacion.objects.create(control=control, evaluacion=preparacion)

	return redirect('usuario:inicio')

def descargar(request, id):
	usuario = request.user
	if not usuario.is_authenticated():
		return redirect('raiz:inicio')

	trabajo = Trabajo.objects.get(id=id)
	response = HttpResponse(content_type='application/ms-excel')

	empresa = trabajo.getNombreEmpresa().replace (" ", "_")
	certificacion = trabajo.getNombreCertificacion().replace (" ", "_")

	response['Content-Disposition'] = 'attachment; filename='+ empresa + '___' + certificacion +'.xlsx'
	xlsx_data = escribirExcel(trabajo)
	response.write(xlsx_data)
	return response

def escribirExcel(trabajo):
	from datetime import datetime
	from django.conf import settings
	import re

	output = stringIOModule()
	workbook = xlsxwriter.Workbook(output)
	worksheet = workbook.add_worksheet('Informe de auditoria')

	###### Estilos
	background = workbook.add_format({'bg_color': '#2C3E50'})
	background2 = workbook.add_format({'bg_color': '#18BC9C'})
	right_align = workbook.add_format({'align': 'right'})
	h1 = workbook.add_format({'font_size': 13, 'bold': True})
	h2 = workbook.add_format({'font_size': 12, 'bold': True})
	h3 = workbook.add_format({'font_size': 11, 'bold': True})

	worksheet.set_column('A:A', 8)
	worksheet.set_column('B:B', 80)
	worksheet.set_column('C:C', 14)
	worksheet.set_column('D:D', 5)
	worksheet.set_column('E:E', 50)

	imagenEncabezado = settings.BASE_DIR + settings.STATIC_URL + 'img/logo.png'
	worksheet.insert_image('A1', imagenEncabezado, {'x_offset': 15, 'y_offset': 10})
	
	worksheet.merge_range('A1:Z8', '', background)
	worksheet.merge_range('A9:Z9', '', background2)
	worksheet.set_row(8, 4)

	evaluacion = trabajo.evaluacion
	preparacion = trabajo.preparacion

	worksheet.write(9, 0, 'Generado: '+ time.strftime("%d/%m/%Y %I:%M:%S %p"))
	worksheet.write(10, 0, trabajo.getNombreCertificacion()+' | '+trabajo.getNombreEmpresa(), h1)

	worksheet.write(12, 0, 'PRIMERA PARTE - PREPARACIÓN', h1)
	worksheet.write(13, 0, 'Numero', h1)
	worksheet.write(13, 1, 'Descripción', h1)
	worksheet.write(13, 2, 'Cumplimiento', h1)
	worksheet.write(13, 3, 'Valor', h1)
	worksheet.write(13, 4, 'Comentario', h1)

	fila = 14
	for dominio in preparacion.certificacion.dominio_set.all():
		worksheet.write(fila, 0, dominio.numero, h2)
		worksheet.write(fila, 1, dominio.nombre, h2)
		fila += 1

		for objetivo in dominio.objetivo_set.all():
			worksheet.write(fila, 0, objetivo.numero, h3)
			worksheet.write(fila, 1, objetivo.nombre, h3)
			fila += 1

			for control in objetivo.control_set.all():
				worksheet.write(fila, 0, control.numero)
				worksheet.write(fila, 1, control.nombre)

				calificacion = Calificacion.objects.get(evaluacion=preparacion, control=control)

				worksheet.write(fila, 2, calificacion.cumplimiento.titulo)
				worksheet.write(fila, 3, calificacion.cumplimiento.id)
				worksheet.write(fila, 4, calificacion.comentario)
				fila += 1

	fila += 3
	worksheet.write(fila, 0, 'SEGUNDA PARTE - ANEXO', h1)

	fila += 1
	worksheet.write(fila, 0, 'Numero', h1)
	worksheet.write(fila, 1, 'Descripción', h1)
	worksheet.write(fila, 2, 'Cumplimiento', h1)
	worksheet.write(fila, 3, 'Valor', h1)
	worksheet.write(fila, 4, 'Comentario', h1)

	fila += 1
	for dominio in evaluacion.certificacion.dominio_set.all():
		worksheet.write(fila, 0, dominio.numero, h2)
		worksheet.write(fila, 1, dominio.nombre, h2)
		fila += 1

		for objetivo in dominio.objetivo_set.all():
			worksheet.write(fila, 0, objetivo.numero, h3)
			worksheet.write(fila, 1, objetivo.nombre, h3)
			fila += 1

			for control in objetivo.control_set.all():
				worksheet.write(fila, 0, control.numero)
				worksheet.write(fila, 1, control.nombre)

				calificacion = Calificacion.objects.get(evaluacion=evaluacion, control=control)

				worksheet.write(fila, 2, calificacion.cumplimiento.titulo)
				worksheet.write(fila, 3, calificacion.cumplimiento.id)
				worksheet.write(fila, 4, calificacion.comentario)
				fila += 1

	workbook.close()
	xlsx_data = output.getvalue()
	return xlsx_data