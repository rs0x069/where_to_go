from django.contrib import admin
from .models import Place, PlaceImage


class PlaceImageInline(admin.TabularInline):
    model = PlaceImage
    fields = ('image', 'order')
    ordering = ('order',)
    extra = 1


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        PlaceImageInline,
    ]
