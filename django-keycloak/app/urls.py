from django.urls import path

from .views import LoginView, ProtectedView

urlpatterns = [
    path("api/login/", LoginView.as_view(), name="login"),
    path("api/protected/", ProtectedView.as_view(), name="protected"),
]
