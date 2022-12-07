from django.db import models


class Client(models.Model):
    prenom = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField()
