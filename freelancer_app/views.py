from django.shortcuts import render
from .forms import *
from .models import *
from django.views.generic import (
    TemplateView, CreateView, UpdateView, ListView, View,
    FormView, DetailView,DeleteView)
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

class ProfileView(ListView):
    model = Profile
    # queryset = Profile.objects.all()
    template_name = 'freelancer_app/profile_list.html'    
    
    def get_queryset(self):
        data = Profile.objects.all()
        return data 


class ProfileCreateView(CreateView):
    template_name = 'freelancer_app/create_profile.html'
    model = Profile
    form_class = ProfileCreateForm
    # success_url = reverse_lazy('freelancer_app:profile')

    def post(self, request):
        if request.method == 'POST':
            form = ProfileCreateForm(request.POST)
            if form.is_valid():
                name = request.POST.get('name')
                email = request.POST.get('email')
                phone_no = request.POST.get('phone_no')
                profile = Profile.objects.create(name = name, email=email, phone_no=phone_no)
                profile.save()
                return HttpResponseRedirect(reverse("freelancer_app:profile"))
            else:
                return HttpResponseRedirect(reverse("freelancer_app:profile"))

class ProfileDetailView(DetailView):
    template_name = 'freelancer_app/profile_detail.html'
    model = Profile

    def get_queryset(self, **kwargs):
        profile_id = self.kwargs.get('pk')
        profile = Profile.objects.filter(id = profile_id)
        return profile


