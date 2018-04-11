from django.contrib.auth import login, authenticate
from home.forms import RegistrationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import DataGovAPI as govapi
from . import GoogleMapsAPI as mapsapi
from home.models import CarPark
from home.models import CarParkPrice
from geopy.distance import vincenty
from . import geocoding
from random import randint

def ResultsView(request):
    form = ''
    start=''
    end=''
    if request.method == 'POST':
        try:
            form = request.POST['date']
            start = request.POST['starttime']
            end = request.POST['endtime']
            pricesort = 1
        except:
            pricesort = 0
        userinput = str(request.POST['pac-input'])
        usergeocode = geocoding.getGeoCode(userinput)
        carparks = CarPark.objects.all()
        results = [] 
        distances = []
        prices = []
        for key in carparks:
            distance = (vincenty((usergeocode[0], usergeocode[1]),(key.lat, key.lng)).meters)
            if (distance <= 1000):
                results.append(key)
                distances.append(format(distance/1000, '.2f'))
                if (pricesort):
                    price = calcPrice(start, end, key)
                    prices.append(format(price, '.2f'))
        if (pricesort):
            print("sorting prices...")
            for x in range(1, len(distances)):
                for y in range(x, 0, -1):
                    if (prices[y] < prices[y-1]):
                        temp = distances[y]
                        distances[y] = distances[y-1]
                        distances[y-1] = temp
                        temp = results[y]
                        results[y] = results[y-1]
                        results[y-1] = temp
                        temp = prices[y]
                        prices[y] = prices[y-1]
                        prices[y-1] = temp
                    else:
                        break
        else:
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
        noresults = len(results)
        if (pricesort):
            results = zip(results, distances, prices)
        else:
            results = zip(results, distances)
        return render(request, 'results/ResultsUI.html', {'datechosen':form,'starttime':start,'endtime':end,'result' : results, "noresults" : noresults, "userinput" : userinput, "pricesorted" : pricesort, "prices" : prices})


    else:
        return HttpResponse("You are not supposed to be here!")

def calcPrice(starttime, endtime, cp):
    start = convertTime(starttime)
    end = convertTime(endtime)
    totaltime = end - start
    try:
        carparkprice = CarParkPrice.objects.get(carPark = cp)
    except:
        carparkprice = "null"
    freeperioddeducted = False
    firsthourdeducted = False
    price = 0
    if (carparkprice != "null"):
        while (totaltime > 0):
            if (carparkprice.perentry > 0):
                return carparkprice.perentry
            elif (carparkprice.freeperiod > 0 and not freeperioddeducted):
                totaltime = totaltime - carparkprice.freeperiod
                freeperioddeducted = True
            elif (carparkprice.firsthour > 0 and not firsthourdeducted):
                totaltime = totaltime - 60
                firsthourdeducted = True
                price = price + carparkprice.firsthour
            elif (carparkprice.subhour > 0):
                if (totaltime < 60 and carparkprice.subhalfhour):
                    totaltime = totaltime - 30
                    price = price + carparkprice.subhalfhour
                elif (totaltime < 60 and carparkprice.subfifteen):
                    totaltime = totaltime - 15
                    price = price + carparkprice.subfifteen
                else:
                    totaltime = totaltime - 60
                    price = price + carparkprice.subhour
            elif (carparkprice.subhalfhour > 0):
                totaltime = totaltime - 30
                price = price + carparkprice.subhalfhour
            elif (carparkprice.subfifteen > 0):
                totaltime = totaltime - 15
                price = price + carparkprice.subfifteen
        return price
    else:
        return ((randint(4, 16))/4)*totaltime/60


def convertTime(time):
    hours = int(time[0:2])
    minutes = int(time[3:5])
    totaltime = hours*60 + minutes
    return totaltime
# Create your views here.
