from django.views.generic.list import ListView
from django.views.generic.base import View, TemplateView, RedirectView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from django import forms
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse

from .models import URL, UserProfile
from .forms import UserForm, UserProfileForm
from extensions.slug_generation import generate_slug

import os

# helper functions


# Create your views here.

class HomeView(ListView):
    model = URL
    ordering = '-visits'
    paginate_by = 10
    template_name = 'URLshortener/home.html'


class AboutUsView(TemplateView):
    template_name = 'URLshortener/about_us.html'


class URLRedirectView(RedirectView):
    permanant = True
    
    def get_redirect_url(self, slug):
        url = get_object_or_404(URL, slug=slug)
        url.increase_visits()
        return url.address


class DashboardView(LoginRequiredMixin, ListView):
    paginate_by = 10
    template_name = 'URLshortener/dashboard.html'

    def get_queryset(self):
        return self.request.user.urls.order_by('-visits')


class AddURLView(LoginRequiredMixin, CreateView):
    template_name = 'URLshortener/add_url.html'
    model = URL
    fields = ['label', 'address']

    def form_valid(self, form):
        url_obj = form.save(commit=False)
        url_obj.slug = generate_slug()
        url_obj.author = self.request.user
        url_obj.save()
        context = self.get_context_data()
        context['shortened_url'] = str(url_obj)
        return self.render_to_response(context)


class DeleteURLView(LoginRequiredMixin, View):
    def get(self, request, slug):
        url_obj = get_object_or_404(URL, slug=slug, author=request.user)
        url_obj.delete()
        redirect_url = self.get_redirect_url()
        return redirect(redirect_url)

    def get_redirect_url(self):
        next_url = self.request.GET.get('next')
        page_num = int(self.request.GET.get('page', 1))
        has_next_page = self.request.GET.get('has_next')
        rem_urls = int(self.request.GET.get('rem_urls', 2))

        dashboard_url = reverse('URLshortener:dashboard')
        home_url = reverse('URLshortener:home')

        if next_url == home_url or next_url == dashboard_url:
            if rem_urls == 1 and has_next_page == 'False' and page_num > 1:
                return '{}?page={}'.format(next_url, page_num - 1)
            else:
                return '{}?page={}'.format(next_url, page_num)
        else:
            return dashboard_url


class ProfileView(LoginRequiredMixin, CreateView):
    model = UserProfile
    fields = ['photo', 'birth_date', 'website']
    template_name = 'URLshortener/profile_completion.html'
    success_url = reverse_lazy('URLshortener:dashboard')

    def get_form(self):
        form = super().get_form()
        form.fields['birth_date'].widget = forms.DateInput(attrs={'type':'date'})
        return form

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.photo = self.request.FILES.get('photo')
        return super().form_valid(form)


class DeletePhotoView(LoginRequiredMixin, View):
    def get(self, request):
        photo_path = request.user.profile.photo.path
        if os.path.exists(photo_path):
            os.remove(photo_path)
        request.user.profile.photo = None
        request.user.profile.save()
        return redirect('URLshortener:dashboard')


class EditProfileView(LoginRequiredMixin, View):
    template_name = 'URLshortener/edit_profile.html'

    def get_context_data(self):
        context = {
            'user_form': UserForm(self.request.POST or None, instance=self.request.user),
            'profile_form': UserProfileForm(self.request.POST or None, 
                self.request.FILES or None, instance=self.request.user.profile),
        }
        return context

    def get(self, request):
        return render(request, self.template_name, self.get_context_data())

    def post(self, request):
        context = self.get_context_data()

        if context['user_form'].is_valid() and context['profile_form'].is_valid():
            context['user_form'].save()
            context['profile_form'].save()
            return redirect('URLshortener:dashboard')
        else:
            return render(request, self.template_name, context)
