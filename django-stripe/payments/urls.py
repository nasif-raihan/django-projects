from django.contrib import admin
from django.urls import path
from payments.views import BuyCoffeeView, StripeWebhookView, success, cancel

urlpatterns = [
    path("admin/", admin.site.urls),
    path("success/", success, name="success"),
    path("cancel/", cancel, name="cancel"),
    path("buy-coffee/", BuyCoffeeView.as_view(), name="buy-coffee"),
    path("stripe/webhook/", StripeWebhookView.as_view(), name="stripe-webhook"),
]
