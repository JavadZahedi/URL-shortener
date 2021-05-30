from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import URL
from .forms import UserProfileForm, URLForm
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
    return redirect(short_url.address, permanant=True)


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
            form.instance.slug = generate_slug()
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
