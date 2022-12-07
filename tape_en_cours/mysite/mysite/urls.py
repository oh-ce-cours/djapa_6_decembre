from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", admin.site.urls),
    path("polls/", include("polls.urls")),
]
