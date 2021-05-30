from django.contrib import admin
from django.urls import path
from . import views

app_name = 'URLshortener'
urlpatterns = [
    path('', views.home, name='home'),
    path('shortened-url/<slug:slug>', views.shortened_url, name='shortened-url'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-url/', views.add_url, name='add-url'),
]