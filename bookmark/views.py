from django.contrib.auth import login, authenticate
from home.forms import RegistrationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse

def BookmarkedCarParkController(request):
    return render(request, 'bookmark/BookmarkedCarParkUI.html')