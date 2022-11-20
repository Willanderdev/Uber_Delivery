from django import forms

from .models import Servicos


class Formendereço(forms.ModelForm):
    class Meta:
        model = Servicos
        fields = ['servicos', 'coleta', 'entrega', 'veiculo', 'status']
