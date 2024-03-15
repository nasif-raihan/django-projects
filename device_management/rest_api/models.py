from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)
    address = models.CharField(max_length=255)
    email = models.EmailField()


EMPLOYEE_DESIGNATIONS = {
    "TL": "Team Lead",
    "PO": "Product Owner",
    "PM": "Project Manager",
    "OA": "Office Assistant",
    "SWE": "Software Engineer",
    "HRM": "Human Resource Manager",
    "SQAE": "Software Quality Assurance Engineer",
    "others": "Others",
}


class Employee(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(choices=EMPLOYEE_DESIGNATIONS, max_length=100)
    email = models.EmailField()
    company = models.ForeignKey(to=Company, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name}-{self.designation}-{self.email}-{self.company.name}"


DEVICE_LIST = {"mobile": "Mobile", "tab": "Tablet", "laptop": "Laptop"}
DEVICE_CONDITION = {
    "new": "New",
    "used": "Used",
    "damaged": "Damaged",
    "faulty": "Faulty",
    "repaired": "Repaired",
}


class Device(models.Model):
    name = models.CharField(max_length=100, choices=DEVICE_LIST)
    condition = models.CharField(choices=DEVICE_CONDITION, max_length=100)


class Checkout(models.Model):
    checkout_date = models.DateTimeField(auto_now_add=True)
    checkout_condition = models.CharField(max_length=100, choices=DEVICE_CONDITION)
    return_date = models.DateTimeField(null=True, blank=True)
    return_condition = models.CharField(
        max_length=100, choices=DEVICE_CONDITION, null=True, blank=True
    )
    device = models.ForeignKey(to=Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(to=Employee, on_delete=models.CASCADE)
    company = models.ForeignKey(to=Company, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.device_name}-{self.device_condition}-{self.employee.name}-{self.company.name}"
