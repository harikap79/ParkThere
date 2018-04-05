from django.contrib.auth import login, authenticate
from home.forms import RegistrationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.models import BookmarkedCarPark

def BookmarkedCarParkView(request):
    bmcarpark=BookmarkedCarPark.objects.filter(user = request.user)
    if request.method == 'POST':
        carparkID=request.POST['chosen']
        print('debug removing bookmarked carpark '+carparkID)
        BookmarkedCarPark.objects.filter(user = request.user,carPark__id=carparkID).delete()
    return render(request, 'bookmark/BookmarkedCarParkUI.html',{'bmcarpark':bmcarpark})
