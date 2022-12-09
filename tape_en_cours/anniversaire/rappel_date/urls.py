from django.urls import path

from . import views

app_name = "anniversaire"

urlpatterns = [
    path("", views.index, name="index"),
    path("details//<int:anniversaire_pk>", views.index, name="index"),
    path("envoie_email/<int:anniversaire_pk>", views.notify, name="notify"),
]
