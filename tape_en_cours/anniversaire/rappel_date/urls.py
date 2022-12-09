from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("notify/<int:pk>", views.notify, name="notify"),
]
