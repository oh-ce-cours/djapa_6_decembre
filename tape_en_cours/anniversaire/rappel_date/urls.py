from django.urls import path

from . import views

app_name = "anniversaire"

urlpatterns = [
    path("", views.index, name="index"),
    path("notify/<int:anniversaire_pk>", views.notify, name="serrdfgfs"),
]
