from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import URL
from .forms import UserForm, UserProfileForm, SignInForm, URLForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from extensions.slug_generation import generate_slug

# Create your views here.

def home(request):
    url_list = URL.objects.order_by('-visits')
    paginator = Paginator(url_list, 10)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    context = {
        'short_urls': page_obj,
    }
    return render(request, 'URLshortener/home.html', context)


def shortened_url(request, slug):
    short_url = get_object_or_404(URL, slug=slug)
    short_url.increase_visits()
    return HttpResponseRedirect(short_url.address)


def sign_up(request):
    if request.user.is_authenticated:
        return redirect('URLshortener:dashboard')

    signed_up = False
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
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
    if request.user.is_authenticated:
        return redirect('URLshortener:dashboard')

    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():        
            login(request, form.signed_in_user)
            return redirect('URLshortener:dashboard')         
    else:
        form = SignInForm()

    return render(request, 'URLshortener/sign_in.html', {'form': form})


@login_required
def dashboard(request):
    url_list = request.user.urls.order_by('-visits')
    paginator = Paginator(url_list, 10)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    context = {
        'short_urls': page_obj,
    }
    return render(request, 'URLshortener/dashboard.html', context)


@login_required
def add_url(request):
    added = False
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            slug = generate_slug()
            form.instance.slug = slug
            form.instance.author = request.user
            url_obj = form.save()
            form.fields['shortened_url'].initial = str(url_obj)
            added = True
    else:
        form = URLForm()

    context = {
        'form': form,
        'added': added,
    }
    return render(request, 'URLshortener/add_url.html', context)


@login_required
def sign_out(request):
    logout(request)
    return redirect('URLshortener:home')