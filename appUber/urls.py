from django.urls import path
from .views import Index, Servico, Solicite
from django.urls import path, include

from django.conf.urls.static import static


urlpatterns = [
    path('', Index, name='index'),
    path('usuarios/', include('django.contrib.auth.urls')),
    path('servicos', Servico, name='servicos'),
    path('solicite', Solicite, name='solicite'),
    # path('profile', Profile, name='profile'),
    # path('editar/<int:id>', Editar, name='editar'),
    # path('editar/delete/<int:id>', Delete, name='delete')

]
