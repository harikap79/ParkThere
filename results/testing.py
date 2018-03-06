import geocoding
import hdbapi

carparks = hdbapi.getHDBCarparks()
for key in carparks:
    print(key['address'])
    hello = geocoding.getGeoCode(key['address'])
    print(hello[0])
    print(hello[1])
