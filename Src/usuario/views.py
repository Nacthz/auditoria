from django.shortcuts import render

def index(request):
	usuario = request.user
	if usuario is not None:
		perfil = usuario.perfil.getTipo()

		#Revisa si es auditor
		if(perfil == 'Auditor'):
			return index_auditor(request, usuario)
		
		#Revisa si es empresa
		if(perfil == 'Empresa'):
			return index_empresa(request, usuario)
		
		#No tiene un perfil valido o no tiene perfil
		return render(request, 'index.html')
	else:
		#No tiene sesion activa
		return render(request, 'login.html')

#Vista index para auditores
def index_auditor(request, usuario):
	datos = {
		'perfil': usuario.perfil,
	}
	return render(request, 'auditor.html', datos)

#Vista index para empresa
def index_empresa(request, usuario):
	datos = {
		'perfil': usuario.perfil,
	}
	return render(request, 'empresa.html', datos)