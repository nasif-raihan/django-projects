from abc import ABC, abstractmethod

from ..model import Company


class CompanyRepository(ABC):
    @abstractmethod
    def add_company(self, company: Company) -> Company:
        raise NotImplemented("Implement add_company method")

    @abstractmethod
    def get_company(self, email: str) -> Company:
        raise NotImplemented("Implement get_company method")

    @abstractmethod
    def get_registered_company_count(self) -> int:
        raise NotImplemented("Implement get_registered_company_count method")
