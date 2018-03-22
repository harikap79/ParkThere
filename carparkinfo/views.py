from django.contrib.auth import login, authenticate
from home.forms import RegistrationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from home.models import CarPark, SearchHistory


def CarParkInfoController(request, id):
        carpark = get_object_or_404(CarPark, id=id)
        if request.user.is_anonymous:
                print('debug anonymous user')
        else:
                print('debug info user' + request.user.email)
                saveHis = SearchHistory()
                saveHis.user=request.user
                saveHis.carPark=carpark
                saveHis.save()
        return render(request, 'carparkinfo/CarParkInfoUI.html', {'carpark' : carpark})
# Create your views here.
