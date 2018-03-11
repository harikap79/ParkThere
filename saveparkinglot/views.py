from django.contrib.auth import login, authenticate
from home.forms import RegistrationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse


def SaveParkingLotController(request):
    print('debug save')
    return render(request, 'saveparkinglot/SaveParkingLotUI.html')

def SavedParkingLotController(request):
    print('debug saved')
    return render(request, 'saveparkinglot/SavedParkingLotUI.html')
# Create your views here.
