from django.http import HttpResponse
from django.template import loader

from places.models import Place


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
                    "placeId": item.id,
                    "detailsUrl": {
                        "title": item.title,
                        "imgs": [],
                        "description_short": item.description_short,
                        "description_long": item.description_long,
                        "coordinates": {
                            "lng": item.coordinate_lng,
                            "lat": item.coordinate_lat
                        }
                    }
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
