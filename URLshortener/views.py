from django.views.generic.list import ListView
from django.views.generic.base import RedirectView
from django.views.generic.edit import FormView, CreateView, UpdateView

from django import forms
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect

from .models import URL, UserProfile
from .forms import URLForm
from extensions.slug_generation import generate_slug


# Create your views here.

class HomeView(ListView):
    queryset = URL.objects.order_by('-visits')
    paginate_by = 10
    template_name = 'URLshortener/home.html'


class URLRedirectView(RedirectView):
    permanant = True
    
    def get_redirect_url(self, slug):
        url = get_object_or_404(URL, slug=slug)
        url.increase_visits()
        return url.address


class DashboardView(ListView):
    paginate_by = 10
    template_name = 'URLshortener/dashboard.html'

    def get_queryset(self):
        return self.request.user.urls.order_by('-visits')


class AddURLView(FormView):
    template_name = 'URLshortener/add_url.html'
    form_class = URLForm

    def get_context_data(self):
        context = super().get_context_data()
        context['added'] = False
        return context

    def form_valid(self, form):
        url_obj = form.save(commit=False)
        url_obj.slug = generate_slug()
        url_obj.author = self.request.user
        url_obj.save()
        context = self.get_context_data()
        context['added'] = True
        context['form'].fields['shortened_url'].initial = str(url_obj)
        return self.render_to_response(context)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data())


class ProfileView(CreateView):
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


class EditProfileView(UpdateView):
    model = UserProfile
    fields = ['photo', 'birth_date', 'website']
    template_name = 'URLshortener/edit_profile.html'
    success_url = reverse_lazy('URLshortener:dashboard')

    def get_object(self):
        return self.request.user.profile

    def get_form(self):
        form = super().get_form()
        form.fields['birth_date'].widget = forms.DateInput(attrs={'type':'date'})
        return form