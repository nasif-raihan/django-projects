from datetime import datetime

from .company import Company
from .device import Device
from .device_condition import DeviceCondition
from .employee import Employee


class Checkout:
    def __init__(
        self,
        checkout_date: datetime,
        checkout_condition: DeviceCondition,
        return_date: datetime | None,
        return_condition: DeviceCondition | None,
        device: Device,
        employee: Employee,
        company: Company,
    ):
        self.checkout_date = checkout_date
        self.checkout_condition = checkout_condition
        self.return_date = return_date
        self.return_condition = return_condition
        self.device = device
        self.employee = employee
        self.company = company
