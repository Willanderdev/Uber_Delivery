from django.contrib import admin

# from django.contrib.auth.admin import UserAdmin

from .forms import Formendereço
from .models import Servicos, Sol_Servicos


@admin.register(Servicos)
class ServicosAdmin(admin.ModelAdmin):
    list_display = ('servicos', 'coleta', 'entrega','veiculo')
    

@admin.register(Sol_Servicos)
class ServicosAdmin(admin.ModelAdmin):
    list_display = ('servicos', 'coleta', 'entrega', 'time',
                    'distancia',  'veiculo', 'valor', 'status')
    
