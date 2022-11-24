
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.base),
    path('', include('other.urls')),  # путь на страницу views.homepage

    path('', include('main1.urls')),  # путь на страницу

]
