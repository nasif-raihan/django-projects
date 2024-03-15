from domain.model import Employee, Company
from domain.repository import EmployeeRepository, CompanyRepository


class AddEmployees:
    def __init__(
        self,
        employee_repository: EmployeeRepository,
        company_repository: CompanyRepository,
    ):
        self.employee_repository = employee_repository
        self.company_repository = company_repository

    def invoke(self, employees: list[Employee], company: Company) -> list[Employee]:
        if self.company_repository.get_company(email=company.email) is None:
            raise RuntimeError(f"The company named {company.name} is not registered")

        added_employees = []
        for employee in employees:
            employee = self.employee_repository.add_employee(
                employee=Employee(
                    name=employee.name,
                    email=employee.email,
                    designation=employee.designation,
                    company=company,
                )
            )
            added_employees.append(employee)
        return added_employees
