from django.urls import path

from . import views

urlpatterns = [
    path("1", views.special_case_2003),
    path("2", views.year_archive),
    path("3", views.year_archive),
    path("4", views.year_archive),
]
