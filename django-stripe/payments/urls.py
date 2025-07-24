from django.contrib import admin
from django.urls import path
from payments.views import BuyCoffeeView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("buy-coffee/", BuyCoffeeView.as_view(), name="buy-coffee"),
]
