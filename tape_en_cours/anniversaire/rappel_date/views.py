from django.shortcuts import render
from .models import Anniversaire

# Create your views here.
def index(request):
    context = {}
    render(request, "rappel_date/index.html", context)
