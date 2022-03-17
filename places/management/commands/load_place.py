import requests
import json

from django.core.management.base import BaseCommand, CommandError
from places.models import Place


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
                places_json = json.loads(data)

                obj, is_created = Place.objects.get_or_create(
                    title=places_json['title'],
                    description_short=places_json['description_short'],
                    description_long=places_json['description_long'],
                    coordinate_lat=places_json['coordinates']['lat'],
                    coordinate_lng=places_json['coordinates']['lng'],
                )

                if not is_created:
                    print("Place doesn't created. The place '%s' is exists" % obj)
