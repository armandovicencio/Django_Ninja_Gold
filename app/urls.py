from django.urls import path
from . import views


app_name = 'juego'

urlpatterns = [
    path('', views.index),
    path('process_money', views.process_money, name='money'),
    path('procesar', views.procesar, name='proceso'),
    path('procesar/<str:valor>', views.procesar),
]