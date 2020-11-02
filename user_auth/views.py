from django_registration.forms import RegistrationForm

# Create your views here.
from .models import User


class CustomUserForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = User
