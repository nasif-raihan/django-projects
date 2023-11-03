from django.urls import path

from employee.views import base

urlpatterns = [path("", base, name="base")]
