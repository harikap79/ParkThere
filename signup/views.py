from django.shortcuts import render
from django.contrib.auth import login, authenticate
from home.forms import RegistrationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse

def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            emailadd = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email = emailadd, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = RegistrationForm()
    return render(request, 'signup/signup.html', {'form': form})
# Create your views here.
