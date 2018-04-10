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
    for carpark in c:
        if carpark.freeParking=='nil':
            carpark.freeParking='No'
        elif carpark.freeParking=='NO':
            carpark.freeParking='No'
        elif carpark.freeParking=='null':
            carpark.freeParking='No'
        if carpark.nightParking=='NO':
            carpark.nightParking='No'
        elif carpark.nightParking=='YES':
            carpark.nightParking='Yes'
        elif carpark.nightParking=='null':
            carpark.nightParking='No'
        elif carpark.nightParking=='nil':
            carpark.nightParking='No'
        carpark.save()
        print('carpark '+carpark.carParkName+' saved')
