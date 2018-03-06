from django.contrib.auth import login, authenticate
from home.forms import RegistrationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render

def searchHistory(request)  :
    return render(request, 'searchhistory/searchhistory.html')
# Create your views here.
