# Generated by Django 4.0.3 on 2022-03-08 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='Заголовок')),
                ('description_short', models.TextField(verbose_name='Короткое описание')),
                ('description_long', models.TextField(verbose_name='Полное описание')),
                ('coordinate_lat', models.DecimalField(decimal_places=15, max_digits=17, verbose_name='Координаты: широта')),
                ('coordinate_lng', models.DecimalField(decimal_places=15, max_digits=17, verbose_name='Координаты: долгота')),
            ],
            options={
                'verbose_name': 'Место',
                'verbose_name_plural': 'Места',
            },
        ),
    ]
