from django.urls import path
from .views import SignUp, Colaborador, Profile, Up_Service, Del_Servico
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('register/', SignUp.as_view(), name='signup'),
    path('colaborador', Colaborador.as_view(), name='colaborador'),
    path('profile', Profile.as_view(), name='profile'),
    path('<int:pk>/Up_Servico/', Up_Service.as_view(), name='up_servico'),
    path('<int:pk>/delete/', Del_Servico.as_view(), name='del_servico'),
]
