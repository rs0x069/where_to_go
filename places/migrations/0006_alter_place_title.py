# Generated by Django 3.2.12 on 2022-03-17 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_alter_place_description_long'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='title',
            field=models.CharField(max_length=64, unique=True, verbose_name='Заголовок'),
        ),
    ]
