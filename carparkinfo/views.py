from django.contrib.auth import login, authenticate
from home.forms import RegistrationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from home.models import CarPark, SearchHistory,BookmarkedCarPark


def CarParkInfoView(request, id):
        carpark = get_object_or_404(CarPark, id=id)
        anon=1
        if request.method !='POST':
                if request.user.is_anonymous:
                        print('debug anonymous user')
                        anon=1
                else:
                        print('debug info user' + request.user.email)
                        saveHis = SearchHistory()
                        saveHis.user=request.user
                        saveHis.carPark=carpark
                        saveHis.save()
                        print('debug save history user: '+saveHis.user.email+' carpark: '+saveHis.carPark.carParkName)
                        anon=0 #not anon

        if request.method == 'POST':
                print('debug bookmarking carpark '+str(carpark.id))
                if BookmarkedCarPark.objects.filter(user=request.user , carPark=carpark).exists():
                        print('debug already exists')
                else:
                        bkm=BookmarkedCarPark()
                        bkm.user=request.user
                        bkm.carPark=carpark
                        bkm.save()
                        print('debug done bookmarking')
                
        return render(request, 'carparkinfo/CarParkInfoUI.html', {'carpark' : carpark , 'anon':anon})
# Create your views here.
