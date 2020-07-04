from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView
from django.urls import path, include
from django.contrib.auth import views as auth_views

from accounts import views

urlpatterns = [
    path('register', views.register_view, name='register'),
    path('', include('django.contrib.auth.urls'), name='login'),
    path('', views.home, name='home')
]