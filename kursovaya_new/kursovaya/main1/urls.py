from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    path('actual/', views.actual, name='actual'),  # путь на страницу views.homepage
    path('carrier/', views.carrier, name='carrier'),  # путь на страницу, где name для указанием URLS в маршрутах
]