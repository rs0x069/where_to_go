import os
import requests

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from urllib.parse import urlparse, unquote

from places.models import Place, PlaceImage


class Command(BaseCommand):
    help = "Add places to DB"

    def add_arguments(self, parser):
        parser.add_argument('url', type=str, help='Give me url with place data as json')

    def handle(self, *args, **options):
        url = options['url']

        response = requests.get(url)
        response.raise_for_status()

        place_content = response.json()

        place_created, is_place_created = Place.objects.get_or_create(
            title=place_content['title'],
            defaults={
                'description_short': place_content['description_short'],
                'description_long': place_content['description_long'],
                'coordinate_lat': place_content['coordinates']['lat'],
                'coordinate_lng': place_content['coordinates']['lng'],
            }
        )

        if not is_place_created:
            print("Place doesn't created. The place '%s' is exists" % place_created)
            return False

        images_url = place_content['imgs']
        for image_url in images_url:
            image_path = urlparse(image_url).path
            image_filename = unquote(os.path.basename(image_path))
            image_response = requests.get(image_url)
            image_response.raise_for_status()

            place_image = PlaceImage(place=place_created)
            place_image.image.save(image_filename, ContentFile(image_response.content), save=False)
            place_image.save()
