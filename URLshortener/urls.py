from django.urls import path
from . import views

app_name = 'URLshortener'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about-us/', views.AboutUsView.as_view(), name='about-us'),
    path('shortened-url/<slug:slug>', views.URLRedirectView.as_view(), name='shortened-url'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('add-url/', views.AddURLView.as_view(), name='add-url'),
    path('edit-url/<slug:slug>', views.EditURLView.as_view(), name='edit-url'),
    path('delete-url/<slug:slug>', views.DeleteURLView.as_view(), name='delete-url'),
    path('profile-completion/', views.ProfileView.as_view(), name='profile-completion'),
    path('delete-photo/', views.DeletePhotoView.as_view(), name='delete-photo'),
    path('edit-profile/', views.EditProfileView.as_view(), name='edit-profile'),
    path('search-dropdown/', views.SearchDropdownView.as_view(), name='search-dropdown'),
]