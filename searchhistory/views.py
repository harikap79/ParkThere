from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from home.models import User, CarPark, SearchHistory


def SearchHistoryView(request):
    rev_history=SearchHistory.objects.filter(user = request.user).order_by('-dateTime')[:30]#order search results in reverse, last 30
    SearchHistory.objects.exclude(pk__in=rev_history).delete() #delete records earlier than last 30 to save space
    #html=''
    #for record in ten_history:
    #   url = '/history/'+str(record.id)+'/'
    #    html += '<a href="' + url + '">' + record.carParkName + '</a><br>'


    return render(request, 'searchHistory/SearchHistoryUI.html', {'revhistory' : rev_history})
