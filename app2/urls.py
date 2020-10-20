from django.urls import path
from .views import Servicedetails
from app2 import views

urlpatterns = [

  path('', views.home, name='home'),
  path('details/<int:pk>', Servicedetails.as_view(), name='service'),
  path('about/', views.aboutus, name='about'),
  path('slider/', views.sliderus, name='slider'),
  path('profile/', views.profile, name='profile'),
  path('team/', views.team, name='team'),

]
