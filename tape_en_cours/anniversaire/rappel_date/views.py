from django.shortcuts import render, redirect
from .models import Anniversaire
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    context = {
        "anniversaires": Anniversaire.objects.filter(),
    }
    return render(request, "rappel_date/index.html", context)


def notify(request, anniversaire_pk):
    if request.method == "POST":
        anniversaire = get_object_or_404(Anniversaire, pk=anniversaire_pk)
        anniversaire.send_email()
    return redirect("anniversaire:index")


def details(request, anniversaire_pk, nom=""):
    anniversaire = get_object_or_404(Anniversaire, pk=anniversaire_pk)
    context = {"item": anniversaire}
    if nom != anniversaire.nom:
        return redirect(
            "anniversaire:details",
            nom=anniversaire.nom,
            anniversaire_pk=anniversaire.pk,
        )

    return render(request, "rappel_date/details.html", context)
