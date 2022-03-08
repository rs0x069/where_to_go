from django.db import models


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
