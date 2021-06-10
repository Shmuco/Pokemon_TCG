from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', views.all, name = 'all'),
    path('newpost', views.NewPost.as_view(), name= 'new_post'),
    path('post<int:post_id>', views.single_post, name= 'single_post'),
    path('post/<slug:pk>/delete', views.DeletePost.as_view(), name= 'delete_post'),
    path('comment/<slug:pk>/delete', views.DeleteComment.as_view(), name= 'delete_comment'),

]