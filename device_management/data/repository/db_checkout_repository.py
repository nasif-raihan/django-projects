from domain.model import Checkout
from domain.repository import CheckoutRepository
from rest_api.models import Checkout as DBCheckout


class DBCheckoutRepository(CheckoutRepository):
    def add_checkout(self, checkout: Checkout) -> Checkout:
        try:
            self.get_checkout(checkout_id=checkout.checkout_id)
        except RuntimeError:
            db_checkout = DBCheckout(
                checkout_condition=checkout.checkout_condition,
                return_date=checkout.return_date,
                return_condition=checkout.return_condition,
                device=checkout.device,
                employee=checkout.employee,
                company=checkout.company,
            )
            return self.to_checkout(db_checkout)
        else:
            return self.update_checkout(checkout)

    def get_checkout(self, checkout_id: int) -> Checkout:
        try:
            db_checkout = DBCheckout.objects.get(id=checkout_id)
        except DBCheckout.DoesNotExist:
            raise RuntimeError("Invalid checkout information")
        else:
            return self.to_checkout(db_checkout)

    def update_checkout(self, checkout: Checkout) -> Checkout:
        try:
            checkout = self.get_checkout(checkout_id=checkout.checkout_id)
        except DBCheckout.DoesNotExist:
            raise RuntimeError("Invalid checkout information")
        else:
            db_checkout = self.to_db_checkout(checkout)
            db_checkout.checkout_condition = checkout.checkout_condition
            db_checkout.return_date = checkout.return_date
            db_checkout.return_condition = checkout.return_condition
            db_checkout.device = checkout.device
            db_checkout.employee = checkout.employee
            db_checkout.company = checkout.company
            db_checkout.save()
        return self.to_checkout(db_checkout)

    @classmethod
    def to_checkout(cls, db_checkout: DBCheckout) -> Checkout:
        return Checkout(
            checkout_id=db_checkout.id,
            checkout_condition=db_checkout.checkout_condition,
            return_date=db_checkout.return_date,
            return_condition=db_checkout.return_condition,
            device=db_checkout.device,
            employee=db_checkout.employee,
            company=db_checkout.company,
        )

    @classmethod
    def to_db_checkout(cls, checkout: Checkout) -> DBCheckout:
        return DBCheckout(
            checkout_condition=checkout.checkout_condition,
            return_date=checkout.return_date,
            return_condition=checkout.return_condition,
            device=checkout.device,
            employee=checkout.employee,
            company=checkout.company,
        )
