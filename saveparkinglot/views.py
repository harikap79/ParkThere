from django.contrib.auth import login, authenticate
from home.forms import SaveLotForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.models import RecordedParkingLot


def SaveParkingLotView(request):
    print('debug save')

    if request.method == 'POST':
        print('debug form')
        form=SaveLotForm(request.POST)
        if form.is_valid():
            print('debug valid form')
            obj = form.save(commit=False)
            print('debug stage 2')
            obj.user = request.user
            print('debug user: '+obj.user.email)
            print('debug carpark: '+obj.carParkName)
            obj.save()
            print('debug stage 3')
            #return HttpResponseRedirect('/thanks/')
            return redirect('/saveparkinglot/saved/')
    else:
        form=SaveLotForm

    return render(request,'saveparkinglot/SaveParkingLotUI.html',{'form':form})
    

def SavedParkingLotView(request):
    print('debug saved')
    
    rec_history= RecordedParkingLot.objects.filter(user = request.user).order_by('-dateTime')[:1]
    #shows only last save
    return render(request, 'saveparkinglot/SavedParkingLotUI.html',{'rechistory':rec_history})
    
        
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
