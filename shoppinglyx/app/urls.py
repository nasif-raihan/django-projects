from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path

from app import forms
from app import views

urlpatterns = [
    path("", views.ProductView.as_view(), name="home"),
    path(
        "product-detail/<int:pk>",
        views.ProductDetailView.as_view(),
        name="product-detail",
    ),
    path("cart/", views.add_to_cart, name="add-to-cart"),
    path("buy/", views.buy_now, name="buy-now"),
    path("profile/", views.profile, name="profile"),
    path("address/", views.address, name="address"),
    path("orders/", views.orders, name="orders"),
    path(
        "password-change/",
        auth_views.PasswordChangeView.as_view(
            template_name="app/password_change.html",
            form_class=forms.UserPasswordChangeForm,
            success_url="/password-change-done/",
        ),
        name="password-change",
    ),
    path(
        "password-change-done/",
        auth_views.PasswordChangeDoneView.as_view(
            template_name="app/password_change_done.html"
        ),
        name="password-change-done",
    ),
    path(
        "password-reset/",
        auth_views.PasswordResetView.as_view(
            template_name="app/password_reset.html",
            form_class=forms.UserPasswordResetForm,
        ),
        name="password-reset",
    ),
    path(
        "password-reset-done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="app/password_reset_done.html"
        ),
    ),
    path(
        "password-reset-confirm/<uid64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="app/password_reset_confirm.html",
            form_class=forms.UserPasswordChangeForm,
        ),
        name="password-reset-confirm",
    ),
    path("mobile/", views.mobile, name="mobile"),
    path("mobile/<slug:slug_field>", views.mobile, name="mobile-slug"),
    path(
        "accounts/login/",
        auth_views.LoginView.as_view(
            template_name="app/login.html", authentication_form=forms.LoginForm
        ),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
    path("registration/", views.RegistrationView.as_view(), name="registration"),
    path("checkout/", views.checkout, name="checkout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
