from django.db import models

# Create your models here.
class Exemple(models.Model):
    email = models.EmailField()

    def send_email(self):
        print("salut")
