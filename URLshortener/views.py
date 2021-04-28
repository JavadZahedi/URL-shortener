from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import URL
from .forms import UserForm, UserProfileForm, SignInForm, URLForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from extensions.utils import generate_slug

# Create your views here.

def home(request):
    context = {
        'short_urls': URL.objects.order_by('-visits'),
    }
    return render(request, 'URLshortener/home.html', context)


def shortened_url(request, slug):
    short_url = get_object_or_404(URL, slug=slug)
    short_url.increase_visits()
    return HttpResponseRedirect(short_url.address)


def sign_up(request):
    signed_up = False
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            login(request, user)
            signed_up = True

    else:
        form = UserForm()

    context = {
        'form': form,
        'signed_up': signed_up,
    }
    return render(request, 'URLshortener/sign_up.html', context)


def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            user = authenticate(username=forms.username, password=forms.password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/dashboard')
                else:
                    messages.error(request, 'حساب کاربری شما فعال نیست')
            else:
                messages.error(request, 'نام کاربری یا رمز عبور اشتباه است')
    else:
        form = SignInForm()

    return render(request, 'URLshortener/sign_in.html', {'form': form})


@login_required
def dashboard(request):
    return render(request, 'URLshortener/dashboard.html', {})


@login_required
def add_url(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            slug = generate_slug()
            form.instance.slug = slug
    else:
        form = URLForm()
    return render(request, 'URLshortener/add_url.html', {form:'form'})


@login_required
def sign_out(request):
    logout(request)
    return HttpResponseRedirect('/')