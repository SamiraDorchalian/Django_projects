from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list_view, name='posts_list'),
    path('<int:pk>/', views.post_detail_view, name='posts_detail'),
]
