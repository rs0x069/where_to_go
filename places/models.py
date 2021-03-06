from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=64, verbose_name="Заголовок", unique=True)
    description_short = models.TextField(blank=True, verbose_name="Короткое описание")
    description_long = HTMLField(blank=True, verbose_name="Полное описание")
    coordinate_lat = models.DecimalField(max_digits=17, decimal_places=15, verbose_name="Координаты: широта",
                                         help_text="latitude, lat")
    coordinate_lng = models.DecimalField(max_digits=17, decimal_places=15, verbose_name="Координаты: долгота",
                                         help_text="longitude, lng")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Места"
        verbose_name = "Место"


class PlaceImage(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images', verbose_name='Место')
    image = models.ImageField(upload_to='images/', verbose_name='Изображение')
    is_active = models.BooleanField(default=True, verbose_name='Активно')
    order = models.PositiveSmallIntegerField(default=0, verbose_name="Сортировка")

    def __str__(self):
        return self.place.title

    @property
    def get_absolute_image_url(self):
        return self.image.url

    class Meta:
        verbose_name_plural = "Фотографии"
        verbose_name = "Фотография"
        ordering = ['order']
