from django.shortcuts import render, redirect
import requests
import json
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate

def home(request):
    url = "https://covid-193.p.rapidapi.com/statistics"

    querystring = {"country":"Indonesia"}

    headers = {
        'x-rapidapi-key': "e6cc85bac1msh9ae13800c251f70p1d18ddjsn456bdf4f50e2",
        'x-rapidapi-host': "covid-193.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring).json()
    
    data = response['response']

    d = data[0]

    print(d)

    context = {
        'cases': d['cases']['total'],
        'deaths': d['deaths']['total'],
        'recovered': d['cases']['recovered']
    }
    return render(request, 'base.html', context)

def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User has been successfully created!')
            return redirect('register')
    else:   
        form = CreateUserForm
    return render(request, 'register.html', {'form' : form})



def prevention(request):
    context = {}
    return render(request, 'prevention.html', context)

def symptoms(request):
    context = {}
    return render(request, 'symptoms.html', context)

def treatments(request):
    context = {}
    return render(request, 'treatments.html', context)

def aboutus(request):
    context = {} 
    return render(request, 'aboutus.html', context)              
