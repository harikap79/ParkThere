from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from home.forms import RegistrationForm
from home.models import SearchHistory, User, CarPark



def get(self,request): 
#   form = RegistrationForm()
#    searchHistory = SearchHistory.objects.all(user=self.User).order_by('-dateTime')[:10]#last ten by this user

   return render(request, 'searchHistory/searchHistory.html')

def post(self, request): 
#    form = RegistrationForm(request.CarPark)
#    if form.is_valid():
#        searchHistory=form.save(commit=False)
#        searchHistory.user=request.user
#        post.save()

#        return redirect('home:home')
    return render(request, 'searchHistory/searchHistory.html')


def searchHistory(request):
    rev_history=SearchHistory.objects.filter(user = request.user).order_by('-dateTime')[:10]#order search results in reverse, last ten
    #html=''
    #for record in ten_history:
    #   url = '/history/'+str(record.id)+'/'
    #    html += '<a href="' + url + '">' + record.carParkName + '</a><br>'


    return render(request, 'searchHistory/searchHistory.html', {'revhistory' : rev_history})
