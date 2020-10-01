from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from .models import Area, Specialty
from django.contrib import messages
from django.views.generic import CreateView
from .forms import DoctorSignUpForm, PatientSignUpForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import User

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

def loginPage(request):

    context = {
        'showLoginBtn' : False
    }

    return render(request, 'eatros/auth/login.html', context)

def register(request):
    # if the user has already loged in
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = PatientSignUpForm()
        if request.method == 'POST':
            form = PatientSignUpForm(request.POST)
            if form.is_valid(): # successfully registered
                user = form.save()
                messages.success(request, 'Account was created for ' + user.username)
                
                return redirect('login.html')
            
        context = {
            'form':form,
            'showLoginBtn' : False
        }
        # not logged in and not POST method
        return render(request, 'eatros/auth/register.html', context) 
