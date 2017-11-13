from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254)
    phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$')

    class Meta:
        model = User
        fields = ('username', 'email', 'phone_number', 'password1', 'password2')