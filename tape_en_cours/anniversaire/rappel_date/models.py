from django.db import models
from django.utils import timezone

# Create your models here.


class Notification(models.Model):
    anniversaire = models.ForeignKey(
        "Anniversaire", related_name="notifications", on_delete=models.CASCADE
    )
    datetime = models.DateTimeField(default=timezone.now)
    message = models.TextField()


class Anniversaire(models.Model):
    email = models.EmailField()
    nom = models.CharField(50)
    prenom = models.CharField(50)
    date = models.DateField()

    def send_email(self):
        print("salut", self.email)
