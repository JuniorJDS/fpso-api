from app.repositories.base_repository import AbstractRepository
from sqlalchemy.orm import Session
from app.repositories.models import Vessels, Equipments, Orders
from app.schemas.schema import Vessel
from typing import Dict


class HelpRepository(AbstractRepository):
    def create_equipment(self, db: Session, equipment: Dict):
        obj = self._equipment(
            name=equipment["name"],
            equipment_code=equipment["code"],
            location=equipment["location"],
            vessel_code=equipment["vessel_code"]
        )
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    def create(self, db: Session, code: str):
        obj = self._vessel(
            code=code
        )
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj
    
    def get_by_code(self, db: Session, code: str):
        return db.query(self._vessel).filter(self._vessel.code == code).first()

    def remove_all(self, db: Session):
        db.query(self._order).delete()
        db.query(self._equipment).delete()
        db.query(self._vessel).delete()
        db.commit()


helpDB = HelpRepository(vessel=Vessels, order=Orders, equipment=Equipments)