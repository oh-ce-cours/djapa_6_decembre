from django.db import models
from django.utils import timezone

# Create your models here.


class Notification(models.Model):
    anniversaire = models.ForeignKey(
        "Anniversaire", related_name="notifications", on_delete=models.CASCADE
    )
    datetime = models.DateTimeField(default=timezone.now)
    message = models.TextField()

    class Meta:
        ordering = ["datetime"]

    def __str__(self):
        return f"{self.anniversaire.nom}, {self.anniversaire.prenom}, {self.datetime}"


class Anniversaire(models.Model):
    owner = models.ForeignKey(User)
    email = models.EmailField()
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    date = models.DateField()

    def send_email(self):
        message = "mon message"
        self.notifications.create(message=message)
        print(message, self.email)

    def __str__(self):
        return f"{self.nom}, {self.prenom}, {self.date}"
