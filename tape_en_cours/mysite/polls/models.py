import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    # ...
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    def __str__(self):
        return self.question_text


from django.db import models

class Question(models.Model):
    # ...

class Choice(models.Model):
    # ...
    def __str__(self):
        return self.choice_text
