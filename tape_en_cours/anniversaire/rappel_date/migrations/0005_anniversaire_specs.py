# Generated by Django 3.2.16 on 2022-12-09 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rappel_date', '0004_auto_20221209_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='anniversaire',
            name='specs',
            field=models.FileField(blank=True, null=True, upload_to='annivs'),
        ),
    ]
