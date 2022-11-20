from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from .forms import Formendereço
from .models import Servicos


@admin.register(Servicos)
class ServicosAdmin(admin.ModelAdmin):
    list_display = ('servicos', 'coleta', 'entrega','veiculo')
