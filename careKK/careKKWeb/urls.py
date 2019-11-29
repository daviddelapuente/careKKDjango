from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('PvsIA', views.PvsIA, name='PvsIA'),
    path('probando', views.probando, name='probando'),
]