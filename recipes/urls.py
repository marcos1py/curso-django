from django.urls import path, include
from recipes import views

urlpatterns = [
    path('', views.home),
    path('contato/', views.contato),
    path('sobre/', views.sobre),
]
