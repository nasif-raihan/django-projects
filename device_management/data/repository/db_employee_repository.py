from domain.model import Employee
from domain.repository import EmployeeRepository
from rest_api.models import Employee as DBEmployee


class DBEmployeeRepository(EmployeeRepository):
    def add_employee(self, employee: Employee) -> Employee:
        try:
            self.get_employee(email=employee.email)
        except RuntimeError:
            db_employee = DBEmployee(
                name=employee.name,
                email=employee.email,
                designation=employee.designation,
                company=employee.company,
            )
            db_employee.save()
            return self.to_employee(db_employee)
        else:
            return self.update_employee(employee)

    def get_employee(self, email: str) -> Employee | None:
        try:
            db_employee = DBEmployee.objects.get(email=email)
        except DBEmployee.DoesNotExsit:
            return None
        return self.to_employee(db_employee)

    def update_employee(self, employee: Employee) -> Employee:
        try:
            employee = self.get_employee(email=employee.email)
            db_employee = self.to_db_employee(employee)
        except DBEmployee.DoesNotExist:
            raise RuntimeError("Invalid employee information")
        else:
            db_employee.name = employee.name
            db_employee.email = employee.email
            db_employee.designation = employee.designation
            db_employee.company = employee.company
            db_employee.save()
        return self.to_employee(db_employee)

    def get_all_employee_by_company(self, company_email: str) -> list[Employee]:
        try:
            db_employees = DBEmployee.objects.filter(company__email=company_email)
        except DBEmployee.DoesNotExit:
            raise RuntimeError("Invalid employee information")
        else:
            return [self.to_employee(db_employee) for db_employee in db_employees]

    @classmethod
    def to_employee(cls, db_employee: DBEmployee) -> Employee:
        return Employee(
            name=db_employee.name,
            email=db_employee.email,
            designation=db_employee.designation,
            company=db_employee.company,
        )

    @classmethod
    def to_db_employee(cls, employee: Employee) -> DBEmployee:
        return DBEmployee(
            name=employee.name,
            email=employee.email,
            designation=employee.designation,
            company=employee.company,
        )
