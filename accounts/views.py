from django.shortcuts import render
from django.urls import reverse_lazy
from . import views
from django.views.generic import CreateView
from . import forms

#we use reverse_lazy to redirect someone when theyre already logged in or logged out , where they should go
# Create your views here.

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    #reverse_lazy lets you reverse only after you sign up , normal reverse would take you back without signing up
    template_name = 'accounts/signup.html'
