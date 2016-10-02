from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from muro.models import Trabajo

def index(request):
	usuario = request.user
	if usuario.is_authenticated():
		perfil = usuario.perfil.getTipo()

		#Revisa si es auditor
		if(perfil == 'Auditor'):
			return index_auditor(request)
		
		#Revisa si es empresa
		if(perfil == 'Empresa'):
			return index_empresa(request)
	else:
		#No tiene sesion activa
		return redirect('usuario:ingresar')

#Vista index para auditores
def index_auditor(request):
	usuario = request.user
	trabajos = Trabajo.objects.filter(auditor=usuario)
	datos = {
		'perfil': usuario.perfil,
		'trabajos': trabajos,
	}
	return render(request, 'auditor.html', datos)

#Vista index para empresa
def index_empresa(request):
	usuario = request.user
	trabajos = Trabajo.objects.filter(empresa=usuario)
	datos = {
		'perfil': usuario.perfil,
		'trabajos': trabajos,
	}
	return render(request, 'empresa.html', datos)

#Vista index para inicio de sesion
def ingresar(request):
	usuario = request.user
	if usuario.is_authenticated():
		return redirect('usuario:inicio')

	error = request.session.pop('error', '')

	datos = {
		'error': error,
	}

	return render(request, 'ingresar.html', datos)

def ingresar_post(request):
	username = request.POST['username']
	password = request.POST['password']

	usuario = authenticate(username=username, password=password)
	if usuario is not None:
		login(request, usuario)
		return redirect('usuario:inicio')
	else:
		request.session['error'] = 'No se pudo iniciar sesión'
		return redirect('usuario:ingresar')

def salir_post(request):
	logout(request)
	return redirect('raiz:inicio')