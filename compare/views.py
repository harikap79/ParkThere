from django.contrib.auth import login, authenticate
from home.forms import RegistrationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import models
from home.models import CarPark


def CompareController(request):
    print('debug compare search')
    searchResults = 0 #default value so later statement wont complain
    searchTerm = 0
    if request.method == 'POST':
        print('debug compare search request made')
        print('debug '+request.POST.get('pac-input'))
        searchResults=searchDB(request.POST.get('pac-input'))
        searchTerm=request.POST.get('pac-input')
    
    #return render(request, 'search/SearchUI.html',{'searchResults' : searchResults})

    return render(request, 'compare/CompareUI.html',{'searchResults':searchResults, 'searchTerm': searchTerm})


def searchDB(searchTerm):
    print('debug searchDB')
    searchResults = CarPark.objects.filter(carParkName__icontains=searchTerm) #| address__icontains(searchTerm))
    for x in searchResults:
        print('debug result: '+x.carParkName)
    return searchResults
