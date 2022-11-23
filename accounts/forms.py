from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm


veículos = [
    (1, 'Moto'),
    (2, 'carro'),
    (3, 'caminhão'),
    (4, 'carreta')
]


class ColaboradorForm(UserCreationForm):
    cpf = forms.IntegerField(label='cpf', required=True)
    veículo = forms.ChoiceField(
        label='Veículo', choices=veículos, required=True)
    
    

    class Meta:
        model = User
        fields = ['username', 'cpf', 'veículo', 'password1', 'password2']
