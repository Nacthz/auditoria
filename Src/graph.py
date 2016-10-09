import sys
from django.apps import apps
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "auditoria.settings")
from django.core.management import execute_from_command_line

outfile = open('sample.png', 'w')

def graph(app):
    app_list = app.split(',')
    outfile.write("digraph G {\n")
    for app in app_list:
        models = apps.get_models(app)
        for model in models:

        # Format the shape
            name = model._meta.object_name
            label = "%s\\n" % name + "\\n".join([field.name for field in model._meta._fields()])
            outfile.write("%s [shape=box,label=\"%s\"];" % (name, label))

            # Draw the relations
            for related in model._meta.get_all_related_objects():
                outfile.write("\t%s -> %s;\n" % (name, related.model._meta.object_name))

            for related in model._meta.get_all_related_many_to_many_objects():
                outfile.write("\t%s -> %s [dir=both];\n" % (name, related.model._meta.object_name))

    outfile.write("}\n")

if __name__=="__main__":
    
    if len(sys.argv) != 2:
        print ("graph.py app1,app2")
        print ("\tWrites a graph of your models suitable for processing with graphviz")
        sys.exit(1)
    graph(sys.argv[1])