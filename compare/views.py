from django.contrib.auth import login, authenticate
from home.forms import RegistrationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.models import CarPark


def CompareController(request):
    allParks=CarPark.objects.all()
    return render(request, 'compare/CompareUI.html',{'allParks' : allParks})
