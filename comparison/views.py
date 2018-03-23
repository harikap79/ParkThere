from django.contrib.auth import login, authenticate
from home.forms import RegistrationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db import models
from django.db.models import Q
from home.models import CarPark


def ComparisonController(request,id=0):
    carpark = get_object_or_404(CarPark, id=id)
    print('debug comparison')
    searchResults = 0 #default value so later statement wont complain
    searchTerm = 0
    notdone=1
    
    
    if id==0:
        print('debug chosen 2 carparks, commencing comparison')
        print('debug carpark 1: '+request.POST.get('prev'))
        print('debug carpark 2: '+request.POST.get('pad-input'))
        notdone=0
    
    if request.method == 'POST':
        print('debug comparison POST')
        print('debug pad input: '+request.POST.get('pad-input'))
        print('debug prev: '+request.POST.get('prev')) 
        searchResults=searchDB(request.POST.get('pad-input'))
        searchTerm=request.POST.get('pad-input')
        prev=request.POST.get('prev')
        notdone=0
    else:
        notdone=1
        prev=0
        
    #return render(request, 'search/SearchUI.html',{'searchResults' : searchResults})

    return render(request, 'comparison/ComparisonUI.html',{'notdone':notdone,'searchResults':searchResults,'searchTerm':searchTerm,'chosen1':carpark,'prev':prev})


def searchDB(searchTerm):
    print('debug searchDB')
    searchResults = CarPark.objects.filter(Q(carParkName__icontains=searchTerm) | Q(id__contains=searchTerm))
    #searchResults = CarPark.objects.filter(carParkName__icontains=searchTerm|id__contains=searchTerm)
    #for x in searchResults:
    #    print('debug result: '+x.carParkName)
    return searchResults
'''
def ComparisonController(request):
    
    print('debug comparison no id')
    searchResults = 0 #default value so later statement wont complain
    searchTerm = 0
    notdone=1
    chosen1=0
    chosen2=0
    
    if request.method == 'POST':
        print('debug comparison no id POST')
        print('debug no id pad input '+request.POST.get('pad-input'))
        print('debug no id prev '+request.POST.get('prev')) 
        searchResults=searchDB(request.POST.get('pad-input'))
        searchTerm=request.POST.get('pad-input')
        chosen1=searchDB(prev)
        notdone=0
    else:
        notdone=1
        
    #return render(request, 'search/SearchUI.html',{'searchResults' : searchResults})

    return render(request, 'comparison/ComparisonUI.html',{'notdone':notdone,'searchResults':searchResults,'searchTerm':searchTerm, 'chosen1':chosen1,'chosen2':chosen2})
'''
