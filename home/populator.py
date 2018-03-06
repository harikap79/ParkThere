import geocoding
import hdbapi


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
    carparks = hdbapi.getHDBCarparks()
    for key in carparks:
        geocode = geocoding.getGeoCode(key['address'])
        print(key['car_park_type'])
        c = CarPark.objects.create(carParkName = key['address'], category = 'null', weekDaysRate1 = 'null', weekDaysRate2 = 'null', satRate = 'null',
                                      sunRate = 'null', carParkType = key['car_park_type'], parkingSystem = key['type_of_parking_system'], freeParking = key['free_parking'],
                                      nightParking = key['night_parking'], lat = geocode[0], lng = geocode[1])
        c.save()
