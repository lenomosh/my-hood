from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from user_auth import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('myHood_Main.urls')),
]
