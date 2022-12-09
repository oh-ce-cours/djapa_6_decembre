from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("notify/<int:anniversary_pk>", views.notify, name="notify"),
]
