from django.shortcuts import render
from .models import Anniversaire

# Create your views here.
def index(request):
    context = {
        "anniversaires": Anniversaire.objects.all(),
    }
    return render(request, "rappel_date/index.html", context)


def notify(request, anniversaire_pk):
    print(anniversaire_pk)
    anniversaire = get_or_404(Anniversaire, pk=anniversaire_pk)
