from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("notify/<int:anniversaire_pk>", views.notify, name="notify"),
]
