from django.contrib.auth import login, authenticate
from home.forms import RegistrationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import DataGovAPI as govapi
from . import GoogleMapsAPI as mapsapi

def results(request):
    if request.method == 'POST':
        userinput = str(request.POST['pac-input'])
        carparks = govapi.getCarParks()
        results = []
        for key in carparks:
            if ("/" in key['carpark']):
                newstring = key['carpark'].split("/")
                newstring = newstring[0]
                if (mapsapi.calcDistance(userinput, newstring) <= 1):
                    results.append(key)
            else:
                if (mapsapi.calcDistance(userinput, key['carpark']) <= 1):
                    results.append(key)
        
        return render(request, 'results/results.html', {'result' : results})


    else:
        return HttpResponse("You are not supposed to be here!")
# Create your views here.
