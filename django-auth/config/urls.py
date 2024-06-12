from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from app.views import UserAPI

router = DefaultRouter()
router.register(prefix="api/user", viewset=UserAPI, basename="user")

urlpatterns = [path("admin/", admin.site.urls), path("", include(router.urls))]
