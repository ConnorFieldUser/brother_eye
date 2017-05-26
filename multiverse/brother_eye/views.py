from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

class LandingView(TemplateView):
    template_name = 'index.html'
