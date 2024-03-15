from enum import Enum


class DeviceCondition(Enum):
    New = "new"
    Used = "used"
    Damaged = "damaged"
    Faulty = "faulty"
    Repaired = "repaired"
