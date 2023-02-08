
from appUber.models import Servicos, Sol_Servicos

from django.contrib.auth.models import User, Group
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from .forms import UserAdminCreationForm
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


class RegisterView(CreateView):
    model = User
    template_name = 'accounts/register.html'
    form_class = UserAdminCreationForm
    success_url = reverse_lazy('login')
    



class Profile(ListView):
    model = Sol_Servicos
    context_object_name = 'servicos'
    template_name = 'accounts/profile.html'
    success_url = reverse_lazy('profile')
   
    def get_context_data(self, *args, **kwargs):
        context = super(Profile, self).get_context_data(*args, **kwargs)
        user = self.request.user
        veiculo = user.veículo
        context['veiculo'] = Sol_Servicos.objects.all().filter(
            veiculo=veiculo)
        context['total'] = Sol_Servicos.objects.all().count()
        context['pending'] = Sol_Servicos.objects.all().filter(
            status='Pending')
        return context


class Up_Service(UpdateView):
    template_name_suffix = "_update_form"
    model = Sol_Servicos
    context_object_name = 'servicos'
    template_name = 'accounts/update.html'
    fields = ['servicos', 'coleta', 'entrega', 'time',
              'distancia',  'veiculo', 'valor', 'status']
    success_url = reverse_lazy('profile')


class Del_Servico(DeleteView):
    template_name_suffix = "_confirm_delete"
    context_object_name = 'servicos'
    model = Sol_Servicos
    template_name = 'accounts/update.html'
    success_url = reverse_lazy('profile')
