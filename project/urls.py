from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from recipes import views

urlpatterns = [
    path('', include("recipes.urls")),
    path('admin/', admin.site.urls),
]
