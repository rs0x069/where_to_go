from django.shortcuts import render
from django.urls import reverse
from slugify import slugify

from places.models import Place
from places.views import get_place


def index(request):
    features = []
    places = Place.objects.all()

    for place in places:
        features.append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.coordinate_lng, place.coordinate_lat]
                },
                "properties": {
                    "title": place.title,
                    "placeId": "{0}-{1}".format(slugify(place.title, max_length=16), place.id),
                    "detailsUrl": reverse(get_place, args=(place.id,))
                }
            }
        )

    places_geojson = {
        "type": "FeatureCollection",
        "features": features
    }

    context = {
        "places": places_geojson
    }

    return render(request, 'index.html', context)
