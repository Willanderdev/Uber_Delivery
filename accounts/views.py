from django.shortcuts import render
from appUber.models import Servicos
from django.contrib.auth.models import User, Group
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from .forms import ColaboradorForm
from django.urls import reverse_lazy


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

    #Adcionando grupo ao usuario criado
    def form_valid(self, form):
        grupo = get_object_or_404(Group, name='Usuario')

        url = super().form_valid(form)
        self.object.groups.add(grupo)
        self.object.save()
        return url

# Adcionando grupo ao colaborador criado
class Colaborador(CreateView):
    template_name = 'registration/colaborador.html'
    form_class = ColaboradorForm
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        grupo = get_object_or_404(Group, name='Colaborador')

        url = super().form_valid(form)
        self.object.groups.add(grupo)
        self.object.save()
        return url


class Profile(ListView):
    model = Servicos
    context_object_name = 'servicos'
    template_name = 'profile.html'
    success_url = reverse_lazy('profile')
   
    def get_context_data(self, *args, **kwargs):
        context = super(Profile, self).get_context_data(*args, **kwargs)
        context['users'] = Servicos.objects.all()
        context['total'] = Servicos.objects.all().count()
        context['pending'] = Servicos.objects.all().filter(status='Pending')
        return context


class Up_Service(UpdateView):
    template_name_suffix = "_update_form"

    model = Servicos
    template_name = 'update.html'
    fields = ['servicos', 'coleta', 'entrega', 'veiculo', 'status']
    success_url = reverse_lazy('profile')


class Del_Servico(DeleteView):
    template_name_suffix = "_confirm_delete"
    context_object_name = 'servicos'
    model = Servicos
    template_name = 'update.html'
    success_url = reverse_lazy('profile')
