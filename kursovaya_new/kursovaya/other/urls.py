
from django.urls import path
from . import views

urlpatterns = [

    path('homepage/', views.homepage, name='homepage'),  # путь на страницу views.homepage
    path('contacts/', views.contacts, name='contacts'),  # путь на страницу
    path('about_the_company/', views.about_the_company, name='about_the_company'),  # путь на страницу

]
