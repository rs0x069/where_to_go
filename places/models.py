from django.db import models

from where_to_go import settings


class Place(models.Model):
    title = models.CharField(max_length=64, verbose_name="Заголовок")
    description_short = models.TextField(verbose_name="Короткое описание")
    description_long = models.TextField(verbose_name="Полное описание")
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
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name='Место')
    image = models.ImageField(upload_to='images/', verbose_name='Изображение')
    is_active = models.BooleanField(default=True, verbose_name='Активно')
    order = models.PositiveSmallIntegerField(default=1, verbose_name="Сортировка")

    @property
    def get_absolute_image_url(self):
        # return "{0}{1}".format(settings.MEDIA_URL, self.image.url)
        return "{0}".format(self.image.url)

    class Meta:
        verbose_name_plural = "Фотографии"
        verbose_name = "Фотография"
