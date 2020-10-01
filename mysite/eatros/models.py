from django.db import models
from django.contrib.auth.models import AbstractUser

class Specialty(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

class Area(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, null=True)

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    phone_number = models.CharField(max_length=20)

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    area = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

