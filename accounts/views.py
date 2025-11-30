from django.shortcuts import render
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import SingUpForm

class SingUpView(CreateView):
    model = User
    form_class = SingUpForm
    template_name = 'accounts/singup.html'
    success_url = reverse_lazy('accounts:login')