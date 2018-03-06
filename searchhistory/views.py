from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from home.forms import RegistrationForm
from home.models import SearchHistory

template_name='home/home.html'#have no idea what this does


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


def index(request):
    ten_history=SearchHistory.objects.all(user=self.User).order_by('-dateTime')#order search results in reverse and take last ten
    template = loader.get_template('searchHistory/searchHistory.html')
    #html=''
    #for record in ten_history:
    #   url = '/history/'+str(record.id)+'/'
    #    html += '<a href="' + url + '">' + record.carParkName + '</a><br>'
    return HttpResponse(template.render(context,request))
