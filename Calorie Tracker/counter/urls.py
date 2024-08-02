
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('nutrition/', views.nutrition_view, name='nutrition'),
]
