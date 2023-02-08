from django import forms

from .models import Servicos, Sol_Servicos


class Formendereço(forms.ModelForm):
    class Meta:
        model = Servicos
        fields = ['servicos', 'coleta', 'entrega', 'veiculo', 'status']


class Formsolicitação(forms.ModelForm):
    class Meta:
        model = Sol_Servicos
        fields = ['servicos', 'coleta', 'entrega', 'time', 'distancia',  'veiculo', 'valor', 'status']
