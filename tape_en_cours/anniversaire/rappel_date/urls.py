from django.urls import path

from . import views

urlpatterns = [
    path("1", views.fbv_python),
    path("2", views.fbv_template),
    path("3", views.fbv_shortcut),
    path("4", views.CBV_verbeux.as_view()),
    path("5", views.CBV_opti.as_view()),
    path("6", views.CBV_complexe.as_view()),
]
