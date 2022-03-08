# Generated by Django 4.0.3 on 2022-03-08 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='coordinate_lat',
            field=models.DecimalField(decimal_places=15, help_text='latitude, lat', max_digits=17, verbose_name='Координаты: широта'),
        ),
        migrations.AlterField(
            model_name='place',
            name='coordinate_lng',
            field=models.DecimalField(decimal_places=15, help_text='longitude, lng', max_digits=17, verbose_name='Координаты: долгота'),
        ),
    ]
