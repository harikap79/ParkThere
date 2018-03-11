from django.contrib.auth import login, authenticate
from home.forms import RegistrationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse


def SearchController(request):
    return render(request, 'search/SearchUI.html')

# Create your views here.
