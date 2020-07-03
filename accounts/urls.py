from django.urls import path, include
from django.contrib.auth import views as auth_views

from accounts import views

urlpatterns = [
    path('register', views.register_view, name='register'),
    path('', include('django.contrib.auth.urls'), name='login'),
    path('reset-password/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='reset-password'),
    path('reset-password-sent/', auth_views.PasswordResetDoneView.as_view(), name='password-reset-done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
    path('reset-password-complete/', auth_views.PasswordResetCompleteView.as_view(), name='password-reset-complete'),
    path('', views.home, name='home')
]