from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('homepage/', views.homepage, name = 'homepage'),
    
    
]