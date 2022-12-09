from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

app_name = "anniversaire"

urlpatterns = [
    path("", login_required(views.index), name="index"),
    path(
        "details/<int:anniversaire_pk>/<str:nom>",
        login_required(views.details),
        name="details",
    ),
    path(
        "envoie_email/<int:anniversaire_pk>",
        login_required(views.notify),
        name="notify",
    ),
]
