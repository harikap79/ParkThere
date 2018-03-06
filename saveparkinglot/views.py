from django.contrib.auth import login, authenticate
from home.forms import RegistrationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse


def saveParkingLot(request):
    return render(request, 'saveparkinglot/saveparkinglot.html')

def savedParkingLot(request):
	return render(request, 'saveparkinglot/savedparkinglot.html')
# Create your views here.
