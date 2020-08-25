from django.urls import path
from .views import *

app_name = 'freelancer_app'

urlpatterns = [
    
    path('', ProfileView.as_view(), name = 'profile'),
    path('create/', ProfileCreateView.as_view(),name = 'create_profile'),
    path('view/<int:pk>/', ProfileDetailView.as_view(), name = 'profile_view'),
    path('update/<int:pk>/', ProfileUpdateView.as_view(), name = 'edit_profile'),
    path('delete/<int:pk>/', ProfileDeleteView.as_view(), name = 'delete_profile'),



]