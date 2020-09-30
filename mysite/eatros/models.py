from django.db import models

class Specialty(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

class Area(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
