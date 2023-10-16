from django.urls import path
from .views import *
from django.views.generic import ListView,DetailView



urlpatterns = [
    path('another_info/about_message/', about_message, name='about_message'),   
    path('another_info/bank/', bank, name='bank'),   
    path('another_info/dop_info/', dop_info, name='dop_info'),   
    path('another_info/el_message/', el_message, name='el_message'),   
  
    
]