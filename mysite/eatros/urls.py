from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('search-doctors/', views.search_doctors, name='search-doctors'),

    path('auth/patient-login.html', views.patient_login, name='patient-login'),
    path('auth/doctor-login.html', views.doctor_login, name='doctor-login'),

    path('auth/patient-register.html', views.patient_register, name='patient-register'),
    path('auth/doctor-register.html', views.doctor_register, name='doctor-register'),

    path('auth/logout.html/', views.logout_user, name='logout-user'),

]