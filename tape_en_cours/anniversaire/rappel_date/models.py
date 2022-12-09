from django.db import models
from django.utils import timezone
from django.conf import settings

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
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    email = models.EmailField()
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    date = models.DateField()
    specs = models.FileField(upload_to="annivs", null=True, blank=True)

    def send_email(self):
        message = "mon message"
        self.notifications.create(message=message)
        print(message, self.email)

    @classmethod
    def get_allowed_for_user(cls, user):
        """ """
        if user.is_superuser:
            anniversaires = cls.objects.all()
        else:
            anniversaires = cls.objects.filter(owner=user)
        return anniversaires

    def __str__(self):
        return f"{self.nom}, {self.prenom}, {self.date}"


def allowed_anniversaire_for_user(user):
    """Cette fonction permet de faire la même chose que
    la méthode de classe dans Anniversaire, définie
    plus haut. Juste elle est dans une fonction
    et pas dans la classe."""
    if user.is_admin:
        anniversaires = Anniversaire.objects.all()
    else:
        anniversaires = Anniversaire.objects.filter(owner=user)
    return anniversaires
