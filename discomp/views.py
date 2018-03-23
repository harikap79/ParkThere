from django.contrib.auth import login, authenticate
from home.forms import RegistrationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db import models
from django.db.models import Q
from home.models import CarPark


def DisCompController(request):

    print('debug discomp')
    print('debug url is: '+request.build_absolute_uri())
    urllist=request.build_absolute_uri().split('/')
    url1=urllist[-3]
    url2=urllist[-2]

    cp1=searchDB(url1)
    cp2=searchDB(url2)
    print('debug cp 1: '+cp1.carParkName+' '+str(cp1.id))
    print('debug cp 2: '+cp2.carParkName+' '+str(cp2.id))
    return render(request, 'discomp/DiscompUI.html',{'cp1':cp1,'cp2':cp2})


def searchDB(searchTerm):
    print('debug searchDB')
    searchResults = CarPark.objects.get(Q(carParkName__icontains=searchTerm) | Q(id__contains=searchTerm))
    #searchResults = CarPark.objects.filter(carParkName__icontains=searchTerm|id__contains=searchTerm)
    #for x in searchResults:
    #    print('debug result: '+x.carParkName)
    return searchResults
