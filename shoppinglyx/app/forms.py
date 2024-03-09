from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    UsernameField,
)
from django.contrib.auth.models import User

from django.utils.translation import gettext_lazy


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password", widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )
    email = forms.CharField(
        required=True,
        label="Email",
        widget=forms.EmailInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        labels = {"password2": "Confirm Password (again)"}
        widgets = {"username": forms.TextInput(attrs={"class": "form-control"})}


class LoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={"class": "form-control", "autofocus": True})
    )
    password = forms.CharField(
        strip=False,
        label=gettext_lazy("Password"),
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "auto-complete": "current-password"},
        ),
    )
