from django.urls import path
from .views import SignUp, Colaborador
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('register/', SignUp.as_view(), name='signup'),
    path('colaborador', Colaborador.as_view(), name='colaborador'),
]
