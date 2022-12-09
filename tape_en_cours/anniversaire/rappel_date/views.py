from django.shortcuts import render, redirect
from .models import Anniversaire
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):

    #####
    # MAUVAISE PRATIQUE : on ne veut pas que cette logique soit dans la vue.
    # 1. ce n'est pas testable
    # 2. ce n'est pas factorisable : on doit le recopier partout

    # if request.user.is_admin:
    #     anniversaires = Anniversaire.objects.all()
    # else:
    #     anniversaires = Anniversaire.objects.filter(owner=request.user)
    ####
    import ipdb

    ipdb.set_trace()
    anniversaires = Anniversaire.get_allowed_for_user(request.user)
    context = {
        "request": request,
        "anniversaires": anniversaires,
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
