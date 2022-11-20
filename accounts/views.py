from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from . forms import ColaboradorForm
from django.urls import reverse_lazy


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'


class Colaborador(CreateView):
    template_name = 'registration/colaborador.html'
    form_class = ColaboradorForm
    success_url = reverse_lazy('login')



