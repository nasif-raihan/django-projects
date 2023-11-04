from django.urls import path

from employee.views import (
    base,
    all_employee,
    add_employee,
    remove_employee,
    filter_employee,
)

urlpatterns = [
    path("", base, name="base"),
    path("all", all_employee, name="all"),
    path("add", add_employee, name="add"),
    path("remove", remove_employee, name="remove"),
    path("filter", filter_employee, name="filter"),
]
