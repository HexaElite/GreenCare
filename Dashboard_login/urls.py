from django.urls import path
from . import views

urlpatterns = [
    path('maindashboard.html', views.maindashboard, name='maindashboard'),
    path('login/', views.login, name='login'),
]
