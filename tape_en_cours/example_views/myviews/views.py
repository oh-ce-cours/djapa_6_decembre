from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

prenoms = ["Matthieu", "Pierre", "Ernest"]

def fbv_python(request):
    inside_ul = "".join([f"<li>{item}</li>" for item in prenoms])
    ul = f"<ul>{inside_ul}</ul>"

    return HttpResponse(ul)

def fbv_template(request):
    pass 

def fbv_shortcut(request):
    pass 

class cbv:
    pass 