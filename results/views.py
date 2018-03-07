from django.contrib.auth import login, authenticate
from home.forms import RegistrationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import DataGovAPI as govapi
from . import GoogleMapsAPI as mapsapi
from home.models import CarPark
from geopy.distance import vincenty
from . import geocoding

def results(request):
    if request.method == 'POST':
        userinput = str(request.POST['pac-input'])
        usergeocode = geocoding.getGeoCode(userinput)
        carparks = CarPark.objects.all()
        results = [] 
        distances = []
        for key in carparks:
            distance = (vincenty((usergeocode[0], usergeocode[1]),(key.lat, key.lng)).meters)
            if (distance <= 1000):
            	results.append(key)
            	distances.append(format(distance/1000, '.2f'))
        for x in range(1, len(distances)):
        	for y in range(x, 0, -1):
        		if (distances[y] < distances[y-1]):
        			temp = distances[y]
        			distances[y] = distances[y-1]
        			distances[y-1] = temp
        			temp = results[y]
        			results[y] = results[y-1]
        			results[y-1] = temp
        		else:
        			break
        results = zip(results, distances)
        return render(request, 'results/results.html', {'result' : results})


    else:
        return HttpResponse("You are not supposed to be here!")
# Create your views here.
