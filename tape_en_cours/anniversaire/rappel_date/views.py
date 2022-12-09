from django.shortcuts import render
from .models import Anniversaire

# Create your views here.
def index(request):
    context = {
        "anniversaires": Anniversaire.objects.all(),
    }
    render(request, "index.html", context)
