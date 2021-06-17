from django import forms
from django.contrib.auth.models import User

from .models import URL, UserProfile

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['photo', 'birth_date', 'website']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type':'date'}),
            'photo': forms.FileInput,
        }
