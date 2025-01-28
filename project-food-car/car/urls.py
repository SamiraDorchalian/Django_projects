from django.urls import path
from . import views
urlpatterns = [
    path('', views.show_home, name='home'),
    path('mwm/', views.show_mwm, name='mwm'),
    path('pars/', views.show_pars, name='pars')
]