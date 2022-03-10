from django.contrib import admin
from .models import Place, PlaceImage


class PlaceImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'place', 'is_active', 'order')
    list_editable = ('order', 'is_active')


admin.site.register(Place)
admin.site.register(PlaceImage, PlaceImageAdmin)
