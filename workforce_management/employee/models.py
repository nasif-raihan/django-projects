from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100, null=False)
    location = models.CharField(max_length=100, default="Remote")

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class Employee(models.Model):
    employee_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.IntegerField(default=50000)
    bonus = models.IntegerField(default=25000)
    hours = models.IntegerField(default=198)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, default="0123456789")
    hire_date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.first_name}, {self.last_name}, {self.phone}"
