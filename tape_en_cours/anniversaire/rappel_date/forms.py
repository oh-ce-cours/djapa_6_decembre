from django.forms import ModelForm
from .models import Anniversaire


class AnniversaireForm(ModelForm):
    class Meta:
        model = Anniversaire
        exclude = ["owner"]
