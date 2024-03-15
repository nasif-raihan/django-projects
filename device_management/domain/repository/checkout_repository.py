from abc import ABC, abstractmethod

from ..model import Checkout


class CheckoutRepository(ABC):
    @abstractmethod
    def add_checkout(self, checkout: Checkout) -> Checkout:
        raise NotImplemented("Implement add_checkout method")

    @abstractmethod
    def get_checkout(self, device_id: int) -> Checkout:
        raise NotImplemented("Implement get_checkout method")

    @abstractmethod
    def update_checkout(self, checkout: Checkout) -> Checkout:
        raise NotImplemented("Implement update_checkout method")
