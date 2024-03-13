from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)
    address = models.CharField(max_length=255)
    email = models.EmailField()

    @staticmethod
    def get_company_names_dict() -> dict:
        names = Company.objects.values_list("name", flat=True)
        company_name_dict = {}
        for name in names:
            company_name_dict[name] = name
        return company_name_dict


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
    company = models.ForeignKey(
        to=Company, on_delete=models.CASCADE, choices=Company.get_company_names_dict()
    )

    def __str__(self) -> str:
        return f"{self.name}-{self.designation}-{self.email}-{self.company.name}"


DEVICE_LIST = {"mobile": "mobile", "tab": "tab", "laptop": "laptop"}
DEVICE_CONDITION_CHOICES = {
    "new": "New",
    "used": "Used",
    "damaged": "Damaged",
    "faulty": "Faulty",
    "repaired": "Repaired",
}


class TakenDeviceHistory(models.Model):
    device_name = models.CharField(choices=DEVICE_LIST, max_length=100)
    taken_date = models.DateTimeField(auto_now_add=True)
    return_data = models.DateTimeField(auto_now=True)
    device_condition = models.CharField(
        choices=DEVICE_CONDITION_CHOICES, max_length=100
    )
    employee = models.ForeignKey(to=Employee, on_delete=models.CASCADE)
    company = models.ForeignKey(to=Company, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.device_name}-{self.device_condition}-{self.employee.name}-{self.company.name}"
