from django import forms
from .models import UserProfile, URL
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError


class UserForm(forms.ModelForm):
    password_repeat = forms.CharField(max_length=4096, widget=forms.PasswordInput,
                                      label='تکرار گذر واژه')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput,
        }

    def clean_password(self):
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

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                self.signed_in_user = user
                return cleaned_data
            else:
                raise ValidationError('حساب کاربری شما فعال نیست')
        else:
            raise ValidationError('نام کاربری یا رمز عبور اشتباه است')


class URLForm(forms.ModelForm):
    class Meta:
        model = URL
        fields = ['address',]
