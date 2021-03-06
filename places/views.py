from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from places.models import Place


def get_place(request, place_id):
    place = get_object_or_404(Place, pk=place_id)

    place_details = {
        "title": place.title,
        "imgs": [image.get_absolute_image_url for image in place.images.all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lat": place.coordinate_lat,
            "lng": place.coordinate_lng,
        }
    }

    return JsonResponse(place_details, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 4})
