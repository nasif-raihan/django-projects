from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect

from accounts.forms import UserForm
from accounts.models import Profile


def signin(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=username, password=password)
            if user is None:
                messages.warning(request, "Account not found.")
            login(request, user=user)
            messages.success(request, f"{username} has signed in successfully.")
            return redirect("/")
    return render(
        request, "accounts/signin.html", context={"title": "Sign In", "form": form}
    )


def signup(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")

            user_obj = User.objects.filter(username=email)
            if user_obj.exists():
                messages.warning(request, "Email is already taken.")

            user_obj = User.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password,
                username=email,
            )
            user_obj.save()
            messages.success(request, "An email has been sent on your mail")
            return HttpResponseRedirect(request.path_info)
        form = UserForm()
    return render(
        request, "accounts/signup.html", context={"title": "Sign Up", "form": form}
    )


def activate_mail(request, email_token):
    try:
        user = Profile.objects.get(email_token=email_token)
        user.is_email_verified = True
        user.save()
        return redirect("/")
    except Profile.DoesnotExist:
        return HttpResponse("Invalid Email Token!")


def signout(request):
    logout(request)
    messages.success(request, f"User signed out successfully")
    return redirect("/")
