from django.contrib import admin
from django.urls import path
from gen import views

urlpatterns = [
    path('',views.home,name = 'home'),
    path('about', views.about),
    path('password',views.password,name='password'),
    path('generatedpassword', views.password, name = 'password'),
    path('profile',views.profile,name='pp'),
]
