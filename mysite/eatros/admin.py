from django.contrib import admin

from .models import Area, Doctor, Patient, Specialty, User

admin.site.register(Area)
admin.site.register(Specialty)
admin.site.register(User)
admin.site.register(Patient)
admin.site.register(Doctor)
