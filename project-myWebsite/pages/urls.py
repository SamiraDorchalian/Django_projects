from django.urls import path
from . import views

urlpatterns = [
    path('/', views.home_page_view, name='home'),
    path('about/', views.about_page_view, name='about'),
    path('contact_us/', views.contactus_page_view, name='contactus'),
]
