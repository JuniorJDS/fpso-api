from app.repositories.base_repository import AbstractRepository
from sqlalchemy.orm import Session
from app.repositories.models import Equipments
from app.schemas.schema import VesselEquipment, EquipmentReturn


class EquipmentsRepository(AbstractRepository):
    def create(self, db: Session, equipment: VesselEquipment):
        obj = self._equipment(
            name=equipment.name,
            equipment_code=equipment.code,
            location=equipment.location,
            vessel_code=equipment.vessel_code

        )
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return EquipmentReturn(**obj.__dict__)
    
    def get_by_vessel(self, db: Session, code: str):
        return db.query(self._equipment).filter(
            self._equipment.vessel_code == code, 
            self._equipment.active == True).all()

    def get_by_code(self, db: Session, code: str):
        return db.query(self._equipment).filter(
            self._equipment.equipment_code == code).first()


equipmentsDB = EquipmentsRepository(equipment=Equipments)