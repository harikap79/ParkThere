from django.contrib.auth import login, authenticate
from home.forms import RegistrationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from home.models import CarPark, SearchHistory,BookmarkedCarPark

def navigateController(request, id):
    carpark = get_object_or_404(CarPark, id=id)
    return render(request, 'navigate/navigateUI.html', {'carpark' : carpark})


# Create your views here.
