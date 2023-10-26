from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('reset_password/', views.reset_password, name='reset_password'),
    path('update_password/', views.update_password, name='update_password'),
]