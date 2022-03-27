from pydantic import BaseModel
from typing import List


class Vessel(BaseModel):
    code: str


class Equipment(BaseModel):
    name: str
    code: str
    location: str


class Order(BaseModel):
    type: str
    cost: float


class VesselEquipment(Equipment):
    vessel_code: str


class EquipmentOrder(Order):
    equipment_code: str


class EquipmentReturn(BaseModel):
    id: int
    name: str
    equipment_code: str
    location: str
    vessel_code: str
    active: bool


class EquipmentsCode(BaseModel):
    equipments_code: List[str]