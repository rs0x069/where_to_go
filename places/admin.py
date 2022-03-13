from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from .models import Place, PlaceImage


class PlaceImageInline(admin.TabularInline):
    model = PlaceImage
    fields = ('image', 'preview_image', 'order')
    ordering = ('order',)
    extra = 1
    readonly_fields = ('preview_image',)

    def preview_image(self, instance):
        return format_html('<img src="{}" height={} />', instance.image.url, '200px')
    preview_image.short_description = "Предосмотр"


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        PlaceImageInline,
    ]
