from django.db import models


class Client(models.Model):
    prenom = models.CharField(max_length=50)
    date_de_naissance = models.DateField()

    def __str__(self):
        return f"{self.prenom} - {self.age} ans"
