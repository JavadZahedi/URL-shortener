from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'URLshortener'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('shortened-url/<slug:slug>', views.URLRedirectView.as_view(),
        name='shortened-url'),
    path('dashboard/', login_required(views.DashboardView.as_view()),
        name='dashboard'),
    path('add-url/', login_required(views.AddURLView.as_view()), name='add-url'),
    path('profile-completion/', login_required(views.ProfileView.as_view()),
        name='profile-completion'),
    path('edit-profile/', login_required(views.EditProfileView.as_view()),
        name='edit-profile'),
]