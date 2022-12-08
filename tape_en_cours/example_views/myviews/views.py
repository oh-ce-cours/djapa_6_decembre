from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

prenoms = ["Matthieu", "Pierre", "Ernest"]

def fbv_python(request):
    inside_ul = "".join([f"<li>{item}</li>" for item in prenoms])
    ul = f"<ul>{inside_ul}</ul>"
    # on peut faire du XSS
    # ul="<script> alert('bouh') </script>"
    return HttpResponse(ul)

def fbv_template(request):
    template = loader.get_template('myviews/index.html')
    context = {
        'prenoms': prenoms,
        "custom": "Dans fbv_template"
    }
    return HttpResponse(template.render(context, request))

def fbv_shortcut(request):
    context = {
        'prenoms': prenoms,
    }
    return render(request, "myviews/index.html", context) 

class cbv:
    pass 