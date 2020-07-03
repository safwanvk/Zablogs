from django.urls import path, include

from accounts import views

urlpatterns = [
    path('register', views.register_view, name='register'),
    path('', include('django.contrib.auth.urls'), name='login'),
    path('', views.home, name='home')
]