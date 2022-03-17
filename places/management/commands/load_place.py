from urllib.parse import urlparse

import requests
import json

from django.core.management.base import BaseCommand, CommandError
from django.core.files.base import ContentFile
from places.models import Place, PlaceImage


class Command(BaseCommand):
    help = "Add places to DB"

    def add_arguments(self, parser):
        parser.add_argument('url', type=str, help='Give me url with place data as json')

    def handle(self, *args, **options):
        url = options['url']

        try:
            response = requests.get(url)
        except requests.RequestException as err:
            print(err)
        else:
            if response.status_code == 200:
                data = json.dumps(response.json())
                place_data = json.loads(data)

                obj, is_created = Place.objects.get_or_create(
                    title=place_data['title'],
                    description_short=place_data['description_short'],
                    description_long=place_data['description_long'],
                    coordinate_lat=place_data['coordinates']['lat'],
                    coordinate_lng=place_data['coordinates']['lng'],
                )

                if not is_created:
                    print("Place doesn't created. The place '%s' is exists" % obj)
                else:
                    images_url = list(place_data['imgs'])

                    for item in images_url:
                        image_filename = urlparse(item).path.split('/')[-1]
                        image_response = requests.get(item)

                        if image_response.status_code == 200:
                            place_image = PlaceImage()
                            place_image.place = obj
                            place_image.image.save(image_filename, ContentFile(image_response.content), save=False)
                            place_image.save()
