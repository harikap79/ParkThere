from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render

from home.forms import RegistrationForm
from home.models import CarPark,SearchHistory,User

template_name='home/home.html'#have no idea what this does

def searchHistory(request)  :
    return render(request, 'searchhistory/searchhistory.html')

def get(self,request): #or this
    form = RegistrationForm()
    carPark=CarPark.objects.all()
    searchHistory=SearchHistory.objects.all()
    user=User.objects.all()

    return render(request, self.template_name)

def post(self, request): #or this
    form = RegistrationForm(request.CarPark)
    if form.is_valid():
        searchHistory=form.save(commit=False)
        searchHistory.user=request.user
        post.save()

        return redirect('home:home')
    return render(request, self.template_name)
