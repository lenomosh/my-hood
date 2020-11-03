from django import forms
from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse
from django_registration.forms import RegistrationForm

# Create your views here.
from myHood_Main.models import Hood
from .models import User


class CustomUserForm(RegistrationForm):
    hood = forms.Select(choices=Hood.objects.all())

    class Meta(RegistrationForm.Meta):
        model = User
        fields = ('username', 'hood_name', 'email', 'password1', 'password2',)


class UserUpdateForm(forms.ModelForm):
    # email = forms.EmailField()
    # # hood = forms.Select(choices=Hood.objects.all())
    # username = forms.CharField(
    #     label='Username',
    #     max_length=30)

    class Meta:
        model = User
        fields = ('hood_name', 'email',)

        # error_messages = {
        #     'username': {
        #         'max_length': 'This value must contain only letters, numbers, hyphens and underscores.'
        #     }
        # }


def profile(request):
    if request.method == "POST":
        user_form = UserUpdateForm(instance=request.user)
        import pdb;
        pdb.set_trace()
        if user_form.is_valid():
            user_form.save()
            messages.success(request, f'Your account has been updated successfully!')
            return redirect('user.profile')
        else:
            return redirect('user.profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        context = dict(user_form=user_form)
        return render(request, 'registration/profile.html', context)
