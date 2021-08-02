from django.contrib import admin
from .import views
from django.urls import path

urlpatterns = [
    path('', views.home),
    path('new/<str:pk>/', views.new),
]
