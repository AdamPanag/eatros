from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User, Doctor, Patient

class PatientSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_patient = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.save()
        patient = Patient.objects.create(user=user)
        patient.phone_number=self.cleaned_data.get('phone_number')
        patient.save()
        return user

class DoctorSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.CharField(required=True)
    area = forms.CharField(required=True)
    specialty = forms.CharField(required=True)
    address = forms.CharField(required=True)


    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_doctor = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.save()
        doctor = Doctor.objects.create(user=user)
        doctor.area=self.cleaned_data.get('area')
        doctor.specialty=self.cleaned_data.get('specialty')
        doctor.address=self.cleaned_data.get('address')
        doctor.save()
        return user
