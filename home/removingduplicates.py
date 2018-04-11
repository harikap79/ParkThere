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
    carpark = CarPark.objects.all()
    for c in carpark:
        c.category=c.category.replace('&amp;','&')
        c.weekDaysRate1=c.weekDaysRate1.replace('&amp;','&')
        c.weekdaysRate2=c.weekDaysRate2.replace('&amp;','&')
        c.freeParking=c.freeParking.replace('&amp;','&')
        c.nightParking=c.nightParking.replace('&amp;','&')
        print(c.carParkName)
        c.save()
        

