from django.urls import path

from .views import (
    RefreshTokenView,
    SendPasswordResetMailView,
    UserChangePasswordView,
    UserListView,
    UserLoginView,
    UserProfileView,
    UserRegistrationView,
)

urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("profile/", UserProfileView.as_view(), name="profile"),
    path("all/", UserListView.as_view(), name="all_users"),
    path("change-password/", UserChangePasswordView.as_view(), name="change_password"),
    path(
        "reset-password-email/",
        SendPasswordResetMailView.as_view(),
        name="reset-password",
    ),
    path("token/refresh/", RefreshTokenView.as_view(), name="refresh_token"),
]
