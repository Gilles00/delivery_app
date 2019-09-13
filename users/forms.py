from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    # Meta class gives information about the model and the fields shown in the form
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        help_texts = {
            'username': None,
            'email': None,
            'password1': None,
            'password2': None,
        }


class UserUpdateForm(forms.Form):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']
        help_texts = {
            'username': None,
            'email': None,
        }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']