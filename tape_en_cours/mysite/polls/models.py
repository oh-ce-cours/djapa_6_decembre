from django.db import models


class Client(models.Model):
    prenom = models.CharField(max_length=50)
    date_de_naissance = models.DateField()

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return f"{self.prenom} - {self.date_de_naissance} ans"
