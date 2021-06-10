from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    

    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('<int:user_id>', views.profile, name='profile'),
    path('<pk>/update', views.UpdateProfile.as_view(), name='profile_update'),
    
]