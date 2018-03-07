from django.contrib.auth import login, authenticate
from home.forms import RegistrationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse


def saveParkingLot(request):
    print('debug save')
    return render(request, 'saveparkinglot/saveparkinglot.html')

def savedParkingLot(request):
    print('debug saved')
    return render(request, 'saveparkinglot/savedparkinglot.html')
# Create your views here.
