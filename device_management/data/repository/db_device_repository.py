from domain.model import Device
from domain.repository import DeviceRepository
from rest_api.models import Device as DBDevice


class DBDeviceRepository(DeviceRepository):
    def add_device(self, device: Device) -> Device:
        try:
            self.get_device(device_id=device.device_id)
        except RuntimeError:
            db_device = DBDevice(name=device.name, condition=device.condition)
            return self.to_device(db_device)
        else:
            return self.update_device(device)

    def get_device(self, device_id: int) -> Device:
        try:
            db_device = DBDevice.objects.get(id=device_id)
        except DBDevice.DoesNotExist:
            raise RuntimeError("Invalid device information")
        else:
            return self.to_device(db_device)

    def update_device(self, device: Device) -> Device:
        try:
            device = self.get_device(device_id=device.device_id)
        except DBDevice.DoesNotExist:
            raise RuntimeError("Invalid device information")
        else:
            db_device = self.to_db_device(device)
            db_device.name = device.name
            db_device.condition = device.condition
            db_device.save()
        return self.to_device(db_device)

    @classmethod
    def to_device(cls, db_device: DBDevice) -> Device:
        return Device(name=db_device.name, condition=db_device.condition)

    @classmethod
    def to_db_device(cls, device: Device) -> DBDevice:
        return DBDevice(name=device.name, condition=device.condition)
