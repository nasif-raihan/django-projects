from django.urls import path

from .views import UserListView, UserLoginView, UserProfileView, UserRegistrationView

urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("profile/", UserProfileView.as_view(), name="profile"),
    path("all/", UserListView.as_view(), name="all_users"),
]
