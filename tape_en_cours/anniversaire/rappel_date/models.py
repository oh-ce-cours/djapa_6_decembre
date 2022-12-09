from django.db import models

# Create your models here.


class Notification(models.Model):
    anniversaire = models.ForeignKey("Anniversaire", on_delete=models.CASCADE)


class Anniversaire(models.Model):
    email = models.EmailField()
    nom = models.CharField(50)
    prenom = models.CharField(50)
    date = models.DateField()

    def send_email(self):
        print("salut", self.email)
