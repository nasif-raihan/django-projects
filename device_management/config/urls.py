from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rest_api.views import (
    CompanyViewSet,
    EmployeeViewSet,
    DeviceViewSet,
    CheckoutViewSet,
)

router = DefaultRouter()
router.register(prefix="company", viewset=CompanyViewSet, basename="company")
router.register(prefix="employee", viewset=EmployeeViewSet, basename="employee")
router.register(prefix="device", viewset=DeviceViewSet, basename="device")
router.register(prefix="checkout", viewset=CheckoutViewSet, basename="checkout")

urlpatterns = [path("admin/", admin.site.urls), path("", include(router.urls))]
