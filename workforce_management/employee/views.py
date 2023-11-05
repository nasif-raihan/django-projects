from datetime import datetime

from django.db.models import Q
from django.http import HttpResponse
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


def remove_employee(request, emp_id=0):
    employees = Employee.objects.all()
    if emp_id:
        try:
            employee_to_be_removed = Employee.objects.get(employee_id=emp_id)
            employee_to_be_removed.delete()
            return HttpResponse(f"Record of ID {emp_id} has been deleted.")
        except Employee.DoesNotExist:
            return HttpResponse("Please enter a valid Employee ID!")
    return render(
        request,
        "employee/remove_employee.html",
        context={"title": "Remove Employee", "employees": employees},
    )


def filter_employee(request):
    if request.method == "POST":
        employee_id = request.POST["employee_id"]
        name = request.POST["name"]
        department = request.POST["department"]
        role = request.POST["role"]
        employees = Employee.objects.all()

        if employee_id and employee_id.isdigit():
            employees = employees.filter(employee_id=int(employee_id))

        if name:
            employees = employees.filter(
                Q(first_name__icontains=name) | Q(last_name__icontains=name)
            )

        if department:
            employees = employees.filter(department__name__icontains=department)

        if role:
            employees = employees.filter(role__name__icontains=role)

        return render(
            request,
            "employee/all_employee.html",
            context={"title": "All Employees", "employees": employees},
        )
    else:
        return render(
            request,
            "employee/filter_employee.html",
            context={"title": "Filter Employee"},
        )
