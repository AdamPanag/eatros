from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search-doctors/', views.search_doctors, name='search-doctors'),
    path('auth/login.html', views.loginPage, name='loginPage'),
    path('auth/register.html', views.register, name='register'),
]