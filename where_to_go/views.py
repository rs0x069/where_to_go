from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from slugify import slugify

from places.models import Place
from places.views import get_place


def index(request):
    template = loader.get_template('index.html')

    features = []
    places = Place.objects.all()

    for item in places:
        features.append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [item.coordinate_lng, item.coordinate_lat]
                },
                "properties": {
                    "title": item.title,
                    "placeId": "{0}-{1}".format(slugify(item.title, max_length=16), item.id),
                    "detailsUrl": reverse(get_place, args=(item.id,))
                }
            }
        )

    places_as_json = {
        "type": "FeatureCollection",
        "features": features
    }

    context = {
        "places": places_as_json
    }

    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)
