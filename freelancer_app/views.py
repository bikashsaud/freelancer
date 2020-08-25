import random

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, FormView,
                                  ListView, TemplateView, UpdateView, View)

from django_seed import Seed

from .forms import *
from .models import *

seeder = Seed.seeder()

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

    def post(self, request):
        if request.method == 'POST':
            form = ProfileCreateForm(request.POST)
            if form.is_valid():
                name = request.POST.get('name')
                email = request.POST.get('email')
                phone_no = request.POST.get('phone_no')
                profile = Profile(name = name, email=email, phone_no=phone_no)
                profile.save()
                # select_data = 
                profile_new = Profile.objects.get(email = email)
                seeder.add_entity(Language, 5, {
                    'user':profile_new,
                    'language':seeder.faker.name(),                    
                    'proficiency':random.choice(('Good','Bad', 'Very Good'))
                })
                seeder.add_entity(Skill, 5, {
                    'user':profile_new,
                    'name':seeder.faker.name(),                    
                    'proficiency':random.choice(('Good','Bad', 'Very Good'))
                })
                seeder.execute()
                return HttpResponseRedirect(reverse("freelancer_app:profile"))
            else:
                return HttpResponseRedirect(reverse("freelancer_app:profile"))

class ProfileDetailView(DetailView):
    template_name = 'freelancer_app/profile_detail.html'
    model = Profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile_id = self.kwargs.get('pk')
        profile = Profile.objects.get(id = profile_id)
        context['profile'] = profile
        skill = Skill.objects.filter(user__id = profile_id)
        context['skill'] = skill
        context['lan'] = Language.objects.filter(user__id = profile_id)
        return context

class ProfileUpdateView(UpdateView):
    template_name = 'freelancer_app/edit_profile.html'
    model = Profile
    form_class = ProfileCreateForm
    success_url = reverse_lazy('freelancer_app:profile')

class ProfileDeleteView(DeleteView):
    model = Profile
    success_url = reverse_lazy('freelancer_app:profile')
