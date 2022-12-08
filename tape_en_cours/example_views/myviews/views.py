from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone

# Create your views here.
from django.views.generic import TemplateView
from typing import Any, Dict


prenoms = ["Matthieu", "Pierre", "Ernest"]


def fbv_python(request):
    inside_ul = "".join([f"<li>{item}</li>" for item in prenoms])
    ul = f"<ul>{inside_ul}</ul>"
    # on peut faire du XSS
    # ul="<script> alert('bouh') </script>"
    return HttpResponse(ul)


def fbv_template(request):
    template = loader.get_template("myviews/index.html")
    context = {"prenoms": prenoms, "custom": "Dans fbv_template"}
    return HttpResponse(template.render(context, request))


def fbv_shortcut(request):
    context = {"prenoms": prenoms, "custom": "Dans fbv_shortcut"}
    return render(request, "myviews/index.html", context)


class CBV_verbeux(TemplateView):
    template_name = "myviews/index.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        return {
            **super().get_context_data(**kwargs),
            "prenoms": prenoms,
            "custom": "Dans CBV verbeux",
        }


class CBV_opti(TemplateView):
    template_name = "myviews/index.html"
    extra_context = {
        "prenoms": prenoms,
        "custom": "Dans CBV opti",
    }


class CBV_complexe(TemplateView):
    """Le dictionnaire extra_contexte est (peut-être ?) créé uniquement
    au lancement de django. La date_extra ne se mettra jamais à jour dans ce cas.
    Dans le get_context_data si l'on n'appelle pas super, on perd le "extra_context".
    """

    template_name = "myviews/index.html"
    extra_context = {
        "prenoms": prenoms,
        "custom": "Dans CBV opti",
        "date_extra": timezone.now(),
    }

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        return {**super().get_context_data(**kwargs), "date": timezone.now()}
