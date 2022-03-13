from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('<int:place_id>/', views.get_place, name='get_place')
]
