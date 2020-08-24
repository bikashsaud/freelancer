from django import forms
from .models import *


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'phone_no']
