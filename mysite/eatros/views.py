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
    if request.user.is_authenticated:
        context = {
            'showLoginBtn' : True
        }
        return render(request, 'eatros/search-doctors.html', context)
    else:
        messages.error(request, 'You must login first.')
        return redirect('/')


def patient_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Wrong username or password.')

    context = {
        'showLoginBtn' : False
    }

    return render(request, 'eatros/auth/patient-login.html', context)


def doctor_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Wrong username or password.')

    context = {
        'showLoginBtn' : False
    }

    return render(request, 'eatros/auth/doctor-login.html', context)


def patient_register(request):
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
                
                return redirect('patient-login.html')
            
        context = {
            'form':form,
            'showLoginBtn' : False
        }
        # not logged in and not POST method
        return render(request, 'eatros/auth/patient-register.html', context)


def doctor_register(request):
    # if the user has already loged in
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = DoctorSignUpForm()
        if request.method == 'POST':
            form = DoctorSignUpForm(request.POST)
            if form.is_valid(): # successfully registered
                user = form.save()
                messages.success(request, 'Account was created for ' + user.username)
                
                return redirect('doctor-login.html')
            
        context = {
            'form':form,
            'showLoginBtn' : False
        }
        # not logged in and not POST method
        return render(request, 'eatros/auth/doctor-register.html', context) 
