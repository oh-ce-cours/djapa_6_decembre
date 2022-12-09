from django.forms import ModelForm, Form 
from .models import Anniversaire

class UploadFile(Form):
    

class AnniversaireForm(ModelForm):
    class Meta:
        model = Anniversaire
        exclude = ["owner"]
