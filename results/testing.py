import geocoding
import hdbapi
import os

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ParkThere.settings")
    from django.db import models
    from . import home
    carparks = hdbapi.getHDBCarparks()
    for key in carparks:
        geocode = getGeoCode(key['address'])
        CarPark.objects.get_or_create(carParkName = key['address'], category = 'null', weekDaysRate1 = 'null', weekDaysDate2 = 'null', satRate = 'null',
                                      sunRate = 'null', carParkType = key['car_park_type'],
                                      parkingSystem = key['type_of_parking_system'], freeParking = key['free_parking'],
                                      nightParking = ['night_parking'], lat = geocode[0], lng = geocode[1])
