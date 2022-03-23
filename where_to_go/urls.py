from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from where_to_go import settings
from where_to_go import views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('places/', include('places.urls')),
    path('tinymce/', include('tinymce.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
