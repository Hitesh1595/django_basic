from django.urls import path,include
from . import forms,views

urlpatterns = [
    path('',views.formpage,name = 'formpage')
]