from django.urls import path

from . import views

urlpatterns = [
    path("1", views.fbv_python),
    path("2", views.fbv_template),
    path("3", views.fbv_shortcut),
    path("4", views.cbv),
]
