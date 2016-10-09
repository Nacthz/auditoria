from django.shortcuts import render
import sys
from django.apps import apps
from django.http import HttpResponse

def index(request):
	return render(request, 'inicio.html')

def graph(request):
	outfile = open('sample.png', 'w+')
	graficar('evaluacion,muro', outfile)
	return HttpResponse("Here's the text of the Web page.")

def graficar(app, outfile):
	app_list = app.split(',')
	outfile.write("digraph G {\n")
	for app in app_list:
		models = apps.get_models(app)
		for model in models:

		# Format the shape
			name = model._meta.object_name
			label = ""

			try:
				label = "%s\\n" % name + "\\n".join([field.name for field in model._meta._fields()])
			except Exception:
				pass

			outfile.write("%s [shape=box,label=\"%s\"];" % (name, label))

			# Draw the relations

			try:
				for related in model._meta.get_all_related_objects():
					outfile.write("\t%s -> %s;\n" % (name, related.model._meta.object_name))
			except Exception:
				pass

			try:
				for related in model._meta.get_all_related_many_to_many_objects():
					outfile.write("\t%s -> %s [dir=both];\n" % (name, related.model._meta.object_name))
			except Exception:
				pass

	outfile.write("}\n")

if __name__=="__main__":

	if len(sys.argv) != 2:
		print ("graph.py app1,app2")
		print ("\tWrites a graph of your models suitable for processing with graphviz")
		sys.exit(1)
	graficar(sys.argv[1], sys.stdout)