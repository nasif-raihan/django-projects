from abc import ABC, abstractmethod

from ..model import Employee


class EmployeeRepository(ABC):
    @abstractmethod
    def add_employee(self, employee: Employee) -> Employee:
        raise NotImplemented("Implement add_employee method")

    @abstractmethod
    def get_employee(self, email: str) -> Employee | None:
        raise NotImplemented("Implement get_employee method")

    @abstractmethod
    def update_employee(self, employee: Employee) -> Employee:
        raise NotImplemented("Implement update_employee method")

    @abstractmethod
    def get_all_employee_by_company(self, company_email: str) -> list[Employee]:
        raise NotImplemented("Implement get_employee_count_by_company method")
