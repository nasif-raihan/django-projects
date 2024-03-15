from .company import Company
from .designation import Designation


class Employee:
    def __init__(
        self, name: str, designation: Designation, email: str, company: Company
    ):
        self.name = name
        self.email = email
        self.designation = designation
        self.company = company
