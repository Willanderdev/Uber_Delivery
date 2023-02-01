from django.urls import path
from .views import SignUp, Profile, Up_Service, Del_Servico, RegisterView
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    
    path('profile', Profile.as_view(), name='profile'),
    path('<int:pk>/Up_Servico/', Up_Service.as_view(), name='up_servico'),
    path('<int:pk>/delete/', Del_Servico.as_view(), name='del_servico'),
]
