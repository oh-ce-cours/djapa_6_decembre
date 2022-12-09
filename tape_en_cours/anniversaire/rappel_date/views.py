from django.shortcuts import render
from .models import Anniversaire
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    context = {
        "anniversaires": Anniversaire.objects.all(),
    }
    return render(request, "rappel_date/index.html", context)


def notify(request, anniversaire_pk):
    anniversaire = get_object_or_404(Anniversaire, pk=anniversaire_pk)
    anniversaire.send_email()
