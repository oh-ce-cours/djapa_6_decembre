from django.shortcuts import render, redirect

from rappel_date.forms import AnniversaireForm, UploadFileForm
from .models import Anniversaire
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _

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
    if request.method == "POST":
        form = AnniversaireForm(request.POST)
        if form.is_valid():
            anniversaire = form.save(commit=False)
            anniversaire.owner = request.user
            anniversaire.save()
    else:
        form = AnniversaireForm(initial={"owner": request.user})

    anniversaires = Anniversaire.get_allowed_for_user(request.user)
    context = {
        "request": request,
        "anniversaires": anniversaires,
        "form": form,
        "message": _("Bienvenue sur le site"),
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


def bulk(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            import ipdb

            ipdb.set_trace()
            return HttpResponseRedirect("/success/url/")
    else:
        form = UploadFileForm()
    return render(request, "upload.html", {"form": form})
