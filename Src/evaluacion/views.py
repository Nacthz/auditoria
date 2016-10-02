from django.shortcuts import render

def ver(request, id):
	return render(request, 'evaluacion.html')