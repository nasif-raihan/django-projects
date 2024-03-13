from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rest_api.views import CompanyView, DeviceView, EmployeeView

router = DefaultRouter()
router.register(prefix="company", viewset=CompanyView, basename="company")
router.register(prefix="employee", viewset=EmployeeView, basename="employee")
router.register(prefix="device", viewset=DeviceView, basename="device")

urlpatterns = [path("admin/", admin.site.urls), path("", include(router.urls))]
