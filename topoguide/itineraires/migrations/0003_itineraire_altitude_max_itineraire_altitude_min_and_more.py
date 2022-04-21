# Generated by Django 4.0.4 on 2022-04-21 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itineraires', '0002_sortie'),
    ]

    operations = [
        migrations.AddField(
            model_name='itineraire',
            name='altitude_max',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='itineraire',
            name='altitude_min',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='itineraire',
            name='altitude_start',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='itineraire',
            name='denivele_negatif',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='itineraire',
            name='denivele_positif',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='itineraire',
            name='description',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='itineraire',
            name='difficulte',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='itineraire',
            name='duree_estimee',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='itineraire',
            name='start',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sortie',
            name='date',
            field=models.DateTimeField(default="2020-11-11 00:00:00"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sortie',
            name='difficulte_ressentie',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sortie',
            name='duree_reelle',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sortie',
            name='groupe_experience',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sortie',
            name='meteo',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sortie',
            name='nombre_personnes',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
