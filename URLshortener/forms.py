from django import forms
from .models import UserProfile, URL
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError


class UserForm(forms.ModelForm):
    password_repeat = forms.CharField(max_length=128, widget=forms.PasswordInput,
                                      label='تکرار گذرواژه')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput,
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_repeat = cleaned_data.get('password_repeat')

        if password != password_repeat:
            raise ValidationError('گذرواژه و تکرار آن با هم برابر نیستند!')
        return cleaned_data


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['photo', 'birth_date']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type':'date'})
        }


class SignInForm(forms.Form):
    username = forms.CharField(max_length=128, label='نام کاربری')
    password = forms.CharField(max_length=128, widget=forms.PasswordInput,
                               label='گذرواژه')

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
            raise ValidationError('نام کاربری یا گذرواژه اشتباه است')


class URLForm(forms.ModelForm):
    shortened_url = forms.URLField(label='نشانی کوتاه شده', disabled=True,
                                   required=False)

    class Meta:
        model = URL
        fields = ['address']
