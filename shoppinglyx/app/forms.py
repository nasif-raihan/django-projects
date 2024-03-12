from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    UsernameField,
    PasswordChangeForm,
    PasswordResetForm,
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


class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label=gettext_lazy("Old Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "current-password",
                "autofocus": True,
                "class": "form-control",
            }
        ),
    )
    new_password1 = forms.CharField(
        label=gettext_lazy("New Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "new-password", "class": "form-control"}
        ),
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=gettext_lazy("Confirm New Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "new-password", "class": "form-control"}
        ),
    )


class UserPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label=gettext_lazy("Email"),
        max_length=254,
        widget=forms.EmailInput(
            attrs={"class": "form-control", "autocomplete": "email"}
        ),
    )
