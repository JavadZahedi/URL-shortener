from django import forms
from .models import UserProfile, URL
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError


class UserForm(forms.ModelForm):
    password = forms.CharField(max_length=255, widget=forms.PasswordInput, label='گذر واژه')
    password_repeat = forms.CharField(max_length=255, widget=forms.PasswordInput,
                                      label='تکرار گذر واژه')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_repeat = cleaned_data.get('password_repeat')

        if password != password_repeat:
            raise ValidationError('رمز عبور و تکرار آن با هم برابر نیستند!')
        return cleaned_data



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['photo', 'birth_date']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type':'date'})
        }


class SignInForm(forms.Form):
    username = forms.CharField(max_length=255, label='نام کاربری')
    password = forms.CharField(max_length=255, widget=forms.PasswordInput, label='رمز عبور')


class URLForm(forms.ModelForm):
    class Meta:
        model = URL
        fields = ['address']
