from django.urls import path, include
from django.contrib.auth import views as auth_views

from accounts import views

urlpatterns = [
    path('register', views.register_view, name='register'),
    path('', include('django.contrib.auth.urls'), name='login'),
    path('reset-password/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='reset-password'),
    path('reset-password-sent/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_sent.html'), name='password-reset-done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_form.html'), name='password-reset-confirm'),
    path('reset-password-done/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_done.html'), name='password-reset-complete'),
    path('', views.home, name='home')
]