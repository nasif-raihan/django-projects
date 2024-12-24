from django.urls import path

from .views import (
    RefreshTokenView,
    SendPasswordResetMailView,
    UserChangePasswordView,
    UserListView,
    UserLoginView,
    UserPasswordResetView,
    UserProfileView,
    UserRegistrationView,
)

urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("profile/", UserProfileView.as_view(), name="profile"),
    path("all/", UserListView.as_view(), name="all-users"),
    path("change-password/", UserChangePasswordView.as_view(), name="change-password"),
    path(
        "reset-password/<str:user_id>/<str:token>/",
        UserPasswordResetView.as_view(),
        name="reset_password",
    ),
    path(
        "reset-password-email/",
        SendPasswordResetMailView.as_view(),
        name="send-mail-reset-password",
    ),
    path("token/refresh/", RefreshTokenView.as_view(), name="refresh-token"),
]
