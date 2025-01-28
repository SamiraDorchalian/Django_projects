from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('pizza/', views.show_pizza, name='pizza'),
    path('rice_chicken/', views.show_rice_chicken, name='rice-chicken'),
    path('hamburger/', views.show_hamburger, name='hamburger'),
]
