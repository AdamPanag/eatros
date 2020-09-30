from django.shortcuts import render

from .models import Area, Specialty

def index(request):
    areas = Area.objects.all()
    specialties = Specialty.objects.all()
    context = {
        'areas' : areas,
        'specialties' : specialties,
        'showLoginBtn' : True
    }

    return render(request, 'eatros/index.html', context)

def search_doctors(request):
    
    return render(request, 'eatros/search-doctors.html', {})

def login(request):

    context = {
        'showLoginBtn' : False
    }

    return render(request, 'eatros/auth/login.html', context)

def register(request):

    context = {
        'showLoginBtn' : False
    }

    return render(request, 'eatros/auth/register.html', context)
