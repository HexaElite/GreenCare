from django.urls import path
from . import views

urlpatterns = [
    path('appointments/', views.appointments, name='appointments'),
    path('registration/', views.registration, name='registration'),
]
