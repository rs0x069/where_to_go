from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings
from . import views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('places/', include('places.urls')),
    path('tinymce/', include('tinymce.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
