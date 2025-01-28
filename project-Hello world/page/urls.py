from django.urls import path, include
from .views import say_something

urlpatterns = [
    path('hi/', say_something, name='something'),
]
