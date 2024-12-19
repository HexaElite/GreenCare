from django.urls import path, include
from . import views



urlpatterns = [
    path('maindashboard/', views.maindashboard, name='maindashboard'),
    path('login/', views.login, name='login'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
]

#urlpatterns = [
 #   path('maindashboard.html', views.maindashboard, name='maindashboard'),
  #  path('login.html', views.login, name='login'),
  #  path('maindashboard.html', views.login_user, name='login_user'),
  #  path('login.html', views.logout_user, name='logout_user'),

#]