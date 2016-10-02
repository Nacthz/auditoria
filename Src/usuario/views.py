from django.shortcuts import render
from muro.models import Trabajo

def index(request):
	usuario = request.user
	if usuario.is_authenticated():
		perfil = usuario.perfil.getTipo()

		#Revisa si es auditor
		if(perfil == 'Auditor'):
			return index_auditor(request, usuario)
		
		#Revisa si es empresa
		if(perfil == 'Empresa'):
			return index_empresa(request, usuario)
	else:
		#No tiene sesion activa
		return render(request, 'login.html')

#Vista index para auditores
def index_auditor(request, usuario):
	trabajos = Trabajo.objects.filter(auditor=usuario)
	datos = {
		'perfil': usuario.perfil,
		'trabajos': trabajos,
	}
	return render(request, 'auditor.html', datos)

#Vista index para empresa
def index_empresa(request, usuario):
	trabajos = Trabajo.objects.filter(empresa=usuario)
	datos = {
		'perfil': usuario.perfil,
		'trabajos': trabajos,
	}
	return render(request, 'empresa.html', datos)