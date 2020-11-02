from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django_registration.backends.one_step.views import RegistrationView

from user_auth import views as user_views
from user_auth.forms import UserRegisterForm
from user_auth.views import CustomUserForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/register/',
         RegistrationView.as_view(
             form_class=CustomUserForm
         ),
         name='user_register',
         ),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('myHood_Main.urls')),
]
