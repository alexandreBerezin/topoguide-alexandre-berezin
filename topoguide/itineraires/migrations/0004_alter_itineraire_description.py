# Generated by Django 4.0.4 on 2022-04-21 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itineraires', '0003_itineraire_altitude_max_itineraire_altitude_min_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itineraire',
            name='description',
            field=models.CharField(max_length=5000),
        ),
    ]
