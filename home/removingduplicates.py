import geocoding
import DataGovAPI


if __name__ == "__main__":
    import os
    import django
    import sys
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(BASE_DIR)
    os.environ['DJANGO_SETTINGS_MODULE'] = 'ParkThere.settings'
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ParkThere.settings")
    django.setup()
    from django.db import models
    from home.models import CarPark
    c = CarPark.objects.all()
    duplicatesremoved = []
    for carpark in c:
        dataset = CarPark.objects.filter(carParkName = carpark.carParkName)
        if (dataset.count() == 3):
            print(carpark.carParkName)
