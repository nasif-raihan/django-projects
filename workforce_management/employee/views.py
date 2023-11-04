from django.shortcuts import render

from .models import Employee


def base(request):
    return render(request, "employee/base.html", context={"title": "Home"})


def all_employee(request):
    employees = Employee.objects.all()
    return render(
        request,
        "employee/all_employee.html",
        context={"title": "All Employees", "employees": employees},
    )


def add_employee(request):
    return render(request, "employee/add_employee.html")


def remove_employee(request):
    return render(request, "employee/remove_employee.html")


def filter_employee(request):
    return render(request, "employee/filter_employee.html")
