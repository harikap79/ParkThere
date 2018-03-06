from django.contrib.auth import login, authenticate
from home.forms import RegistrationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse



# def signup(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             emailadd = form.cleaned_data.get('email')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(email = emailadd, password=raw_password)
#             login(request, user)
#             return redirect('/')
#     else:
#         form = RegistrationForm()
#     return render(request, 'home/signup.html', {'form': form})

# def search(request):
#     return render(request, 'home/search.html')

# def results(request):
#     if request.method == 'POST':
#         userinput = str(request.POST['pac-input'])
#         carparks = govapi.getCarParks()
#         results = []
#         for key in carparks:
#             if ("/" in key['carpark']):
#                 newstring = key['carpark'].split("/")
#                 newstring = newstring[0]
#                 if (mapsapi.calcDistance(userinput, newstring) <= 1):
#                     results.append(key)
#             else:
#                 if (mapsapi.calcDistance(userinput, key['carpark']) <= 1):
#                     results.append(key)
        
#         return render(request, 'home/results.html', {'result' : results})


#     else:
#         return HttpResponse("You are not supposed to be here!")

# def compare(request):
#     return render(request, 'home/compare.html')

# def bookmark(request):
#     return render(request, 'home/bookmark.html')

# def saveParkingLot(request):
#     return render(request, 'home/saveparkinglot.html')

# def savedParkingLot(request):
#     return render(request, 'home/savedparkinglot.html')

# def searchHistory(request)  :
#     return render(request, 'home/searchhistory.html')


