from django.contrib import admin
from django.urls import path
from . import views

app_name = 'URLshortener'
urlpatterns = [
    path('', views.home, name='home'),
    path('shortened-url/<slug:slug>', views.shortened_url, name='shortened-url'),
    path('sign-up/', views.sign_up, name='sign-up'),
    path('sign-in/', views.sign_in, name='sign-in'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('sign-out/', views.sign_out, name='sign-out'),
    path('add-url/', views.add_url, name='add-url'),
]