# Generated by Django 3.2.16 on 2022-12-07 11:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='age',
        ),
        migrations.AddField(
            model_name='client',
            name='date_de_naissance',
            field=models.DateField(default=datetime.date(2022, 12, 7)),
            preserve_default=False,
        ),
    ]