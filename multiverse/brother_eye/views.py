from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView


class LandingView(TemplateView):
    template_name = 'index.html'


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/"
