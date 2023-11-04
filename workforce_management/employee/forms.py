from django.forms import ModelForm

from employee.models import Employee


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = (
            "employee_id",
            "department",
            "first_name",
            "last_name",
            "role",
            "phone",
            "salary",
            "bonus",
        )
        labels = (
            "Employee ID",
            "Department",
            "First Name",
            "Last Name",
            "Role",
            "Phone",
            "Salary",
            "Bonus",
        )
