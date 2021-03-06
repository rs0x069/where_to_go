# Generated by Django 4.0.3 on 2022-03-13 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_placeimage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='placeimage',
            options={'ordering': ['order'], 'verbose_name': 'Фотография', 'verbose_name_plural': 'Фотографии'},
        ),
        migrations.AlterField(
            model_name='placeimage',
            name='order',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Сортировка'),
        ),
    ]
