# File: MyBlog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),  # Home page
    path('posts/', views.post_list, name='post_list'),  # List of blog posts
    path('post/<int:pk>/', views.post_detail, name='post_detail'),  # Single blog post detail
]
