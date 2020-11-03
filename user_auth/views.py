from django import forms
from django_registration.forms import RegistrationForm

# Create your views here.
from myHood_Main.models import Hood
from .models import User


class CustomUserForm(RegistrationForm):
    hood = forms.Select(choices=Hood.objects.all())

    class Meta(RegistrationForm.Meta):
        model = User
