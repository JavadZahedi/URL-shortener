from django import forms
from .models import UserProfile, URL
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['photo', 'birth_date']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type':'date'})
        }


class URLForm(forms.ModelForm):
    shortened_url = forms.URLField(label='نشانی کوتاه شده', disabled=True,
                                   required=False)

    class Meta:
        model = URL
        fields = ['address']
