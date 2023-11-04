from datetime import datetime

from django.shortcuts import render

from .forms import EmployeeForm
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
    today = datetime.now()
    form = EmployeeForm()
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()

    return render(
        request,
        "employee/add_employee.html",
        context={"title": "Add Employee", "today": today, "form": form},
    )


def remove_employee(request):
    return render(request, "employee/remove_employee.html")


def filter_employee(request):
    return render(request, "employee/filter_employee.html")
