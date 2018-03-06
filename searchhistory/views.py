from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render

from home.forms import RegistrationForm
from home.models import SearchHistory

template_name='home/home.html'#have no idea what this does

def searchHistory(request)  :
    return render(request, 'searchhistory/searchhistory.html')

def get(self,request): #or this
    form = RegistrationForm()
    searchHistory = SearchHistory.objects.all(user=self.User).order_by('-dateTime')[:10]#last ten by this user

    return render(request, self.template_name)

def post(self, request): #or this
    form = RegistrationForm(request.CarPark)
    if form.is_valid():
        searchHistory=form.save(commit=False)
        searchHistory.user=request.user
        post.save()

        return redirect('home:home')
    return render(request, self.template_name)
