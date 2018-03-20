from django.contrib.auth import login, authenticate
from home.forms import SaveLotForm
from django.shortcuts import render, redirect
from django.http import HttpResponse


def SaveParkingLotController(request):
    print('debug save')

    if request.method == 'POST':
        print('debug form')
        form=SaveLotForm(request.POST)
        if form.is_valid():
            print('debug valid form')
            print('debug name: '+form.cleaned_data['carpark_name'])
            print('debug level: '+form.cleaned_data['carpark_level'])
            print('debug zone: '+form.cleaned_data['carpark_zone'])
            print('debug lot: '+form.cleaned_data['carpark_lot'])
            #return HttpResponseRedirect('/thanks/')
            return render(request,'saveparkinglot/SavedParkingLotUI.html',)
    else:
        form=SaveLotForm

    return render(request,'saveparkinglot/SaveParkingLotUI.html',{'form':form})
    

def SavedParkingLotController(request):
    print('debug saved')
    return render(request, 'saveparkinglot/SavedParkingLotUI.html')
# Create your views here.
'''def get_form(request):
    if request.method == 'POST':
        form=SaveLotForm(request.POST)
        if form.is_valid():
            print('debug valid form')
            #return HttpResponseRedirect('/thanks/')
    else:
        form=SaveLotForm

    return render(request,'saveparkinglot/SaveParkingLotUI.html',{'form':form})
'''
