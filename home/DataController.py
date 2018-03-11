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
    carparks = DataGovAPI.getCarParks()
    for key in carparks:
        geocode = geocoding.getGeoCode(key['carpark'])
        print(key['carpark'])
        c = CarPark.objects.create(carParkName = key['carpark'], category = key['category'], weekDaysRate1 = key['weekdays_rate1'], weekDaysRate2 = key['weekdays_rate2'], satRate = key['saturday_rate'],
                                      sunRate = key['sunday_public_holiday_rate'], carParkType = 'null', parkingSystem = 'null', freeParking = 'null',
                                      nightParking = 'null', lat = geocode[0], lng = geocode[1])
        c.save()
