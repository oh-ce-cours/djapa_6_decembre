from django.db import models
from django.utils import timezone

# Create your models here.


class Notification(models.Model):
    anniversaire = models.ForeignKey(
        "Anniversaire", related_name="notifications", on_delete=models.CASCADE
    )
    datetime = models.DateTimeField(default=timezone.now)
    message = models.TextField()

    def __str__(self):
        return f"{self.anniversaire.nom}, {self.anniversaire.prenom}, {self.anniversaire.date}"


class Anniversaire(models.Model):
    email = models.EmailField()
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    date = models.DateField()

    def send_email(self):
        print("salut", self.email)

    def __str__(self):
        return f"{self.nom}, {self.prenom}, {self.date}"
