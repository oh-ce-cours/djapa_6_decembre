from django.forms import ModelForm, Form
from django import forms
from .models import Anniversaire


class UploadFile(Form):
    file = forms.FileField()


class AnniversaireForm(ModelForm):
    class Meta:
        model = Anniversaire
        exclude = ["owner"]
