from django.urls import path
from user_auth import views

urlpatterns = [
    path('profile', views.profile, name='user.profile')
]