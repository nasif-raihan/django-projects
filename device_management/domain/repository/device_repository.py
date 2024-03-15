from abc import ABC, abstractmethod

from ..model import Device


class DeviceRepository(ABC):
    @abstractmethod
    def add_device(self, device: Device) -> Device:
        raise NotImplemented("Implement add_device method")

    @abstractmethod
    def get_device(self, device_id: int) -> Device:
        raise NotImplemented("Implement get_device method")

    @abstractmethod
    def update_device(self, device: Device) -> Device:
        raise NotImplemented("Implement update_device method")
