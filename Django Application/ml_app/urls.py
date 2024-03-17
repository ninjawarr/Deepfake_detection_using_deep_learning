"""project_settings URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from . import views,about,predict_page,cuda_full

app_name = 'ml_app'

urlpatterns = [
     path('', index, name='home'),
   path('about/', about, name='about'),
    path('predict/', predict_page, name='predict'),
    path('cuda_full/',cuda_full,name='cuda_full'),
]



