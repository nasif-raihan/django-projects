from domain.model import Company
from domain.repository import CompanyRepository
from rest_api.models import Company as DBCompany


class DBCompanyRepository(CompanyRepository):
    def add_company(self, company: Company) -> Company:
        try:
            company = self.get_company(email=company.email)
        except RuntimeError:
            db_company = DBCompany(
                name=company.name,
                address=company.address,
                email=company.email,
            )
            return self.to_company(db_company)
        else:
            return self.update_company(company)

    def get_company(self, email: str) -> Company:
        try:
            db_company = DBCompany.objects.get(email)
        except DBCompany.DoesNotExist:
            raise RuntimeError("Invalid company information")
        else:
            return self.to_company(db_company)

    def update_company(self, company: Company) -> Company:
        try:
            company = self.get_company(email=company.email)
        except DBCompany.DoesNotExist:
            raise RuntimeError("Invalid company information")
        else:
            db_company = self.to_db_company(company)
            db_company.name = company.name
            db_company.address = company.address
            db_company.email = company.email
            db_company.save()
        return self.to_company(db_company)

    @classmethod
    def to_company(cls, db_company: DBCompany) -> Company:
        return Company(
            name=db_company.name,
            address=db_company.address,
            email=db_company.email,
        )

    @classmethod
    def to_db_company(cls, company: Company) -> DBCompany:
        return DBCompany(
            name=company.name,
            address=company.address,
            email=company.email,
        )
