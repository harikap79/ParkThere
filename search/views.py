from django.contrib.auth import login, authenticate
from home.forms import RegistrationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse


def search(request):
    return render(request, 'search/search.html')

# Create your views here.
